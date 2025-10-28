from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database import init_db, AsyncSessionLocal, User 

import os

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db

@app.on_event("startup")
async def startup_event():
    await init_db()

class UserLogin(BaseModel):
    username: str
    password: str
    role: str

@app.get("/", response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def root():
    return "/login.html"

@app.post("/login")
async def login(user_data: UserLogin, db: AsyncSession = Depends(get_db)):
    
    query = select(User).where(
        (User.username == user_data.username) &
        (User.password == user_data.password) &
        (User.role == user_data.role)
    )
    result = await db.execute(query)
    user = result.scalars().first() # Obtiene el objeto User si existe

    if user:
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
app.mount("/", StaticFiles(directory="Web", html=True), name="web")