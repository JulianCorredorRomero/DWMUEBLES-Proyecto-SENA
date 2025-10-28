# Este archivo se llama main.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# 🔑 CORRECCIÓN: CAMBIAMOS A IMPORTACIÓN DIRECTA
from database import init_db, AsyncSessionLocal, User 

import os

# ----------------------------
# ✅ Configuración de la App
# ----------------------------
app = FastAPI() 

# ----------------------------
# ✅ Configuración de CORS
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# 🔑 FUNCIÓN PARA OBTENER LA SESIÓN DE BD
# ----------------------------
# Esto inyecta una sesión de BD en las rutas que lo necesiten
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db

# ----------------------------
# 🔑 EVENTO DE INICIO: Inicializa la BD (crea tabla y usuarios por defecto)
# ----------------------------
@app.on_event("startup")
async def startup_event():
    await init_db()

# ----------------------------
# ✅ Modelo de Datos (Pydantic)
# ----------------------------
class UserLogin(BaseModel):
    username: str
    password: str
    role: str

# ----------------------------
# ✅ Ruta Principal (Fuerza la redirección a login.html)
# ----------------------------
@app.get("/", response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def root():
    # Cuando el usuario accede a http://127.0.0.1:8000/,
    # esta ruta lo redirige inmediatamente a /login.html
    return "/login.html"


# ----------------------------
# ✅ Ruta de API para el Login (Usa la Base de Datos)
# ----------------------------
@app.post("/login")
async def login(user_data: UserLogin, db: AsyncSession = Depends(get_db)):
    
    # 1. Consulta a la base de datos usando SQLAlchemy ORM
    query = select(User).where(
        (User.username == user_data.username) &
        (User.password == user_data.password) &
        (User.role == user_data.role)
    )
    result = await db.execute(query)
    user = result.scalars().first() # Obtiene el objeto User si existe

    if user:
        # El resto de la lógica de redirección
        redirectPage = "/index.html"
        if user.role == "Carpintero":
            redirectPage = "/carpintero.html"
        elif user.role == "Administrador":
            redirectPage = "/administrador.html"
        
        return {
            "success": True,
            "message": f"Bienvenido {user.username}",
            "redirectUrl": redirectPage
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail={"success": False, "message": "Usuario, contraseña o rol incorrectos"}
        )
# ----------------------------
# ✅ Montaje de Archivos Estáticos
# ----------------------------
# La ruta "/" ahora es manejada por la función 'root' de arriba.
app.mount("/", StaticFiles(directory="Web", html=True), name="web")