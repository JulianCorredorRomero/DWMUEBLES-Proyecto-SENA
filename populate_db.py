import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# Importamos la configuración y los modelos desde database.py
from database import engine, Base, AsyncSessionLocal, User, Task

# --- LÓGICA DE GENERACIÓN DE DATOS MASIVOS ---

async def populate_data(session: AsyncSession):
    """Genera y añade 102 usuarios y tareas de ejemplo a la sesión."""
    
    print("--- 1. Generando 102 usuarios ---")
    default_users = []

    # 1. 90 Clientes (cliente1 a cliente90)
    for i in range(1, 91):
        default_users.append(User(
            username=f"cliente{i}", 
            password="pass", 
            role="Cliente"
        ))
    
    # 2. 8 Carpinteros (incluye a maria)
    carpenter_names = ["maria"] + [f"carpintero{i}" for i in range(2, 9)]
    for name in carpenter_names:
        password = "5678" if name == "maria" else "pass"
        default_users.append(User(
            username=name, 
            password=password, 
            role="Carpintero"
        ))
        
    # 3. 4 Administradores (incluye a admin)
    admin_names = ["admin"] + [f"admin{i}" for i in range(2, 5)]
    for name in admin_names:
        password = "admin123" if name == "admin" else "pass"
        default_users.append(User(
            username=name, 
            password=password, 
            role="Administrador"
        ))

    # 4. Tareas de ejemplo
    default_tasks = [
        Task(title="Reparación de Mesa", description="Arreglar pata rota en mesa de comedor.", status="Pendiente", carpenter_assigned="maria", is_urgent=True),
        Task(title="Diseño de Gabinetes", description="Crear gabinetes a medida para cocina principal.", status="En Progreso", carpenter_assigned="carpintero2"),
        Task(title="Instalación de Estantes", description="Instalar 5 estantes flotantes en sala.", status="Pendiente", carpenter_assigned="carpintero3"),
        Task(title="Restauración de Silla Antigua", description="Lijar y barnizar silla de roble.", status="Finalizada", carpenter_assigned="maria"),
    ]
    
    print(f"Total de Usuarios generados: {len(default_users)}")
    print(f"Total de Tareas generadas: {len(default_tasks)}")

    # 5. Agregar y confirmar
    session.add_all(default_users)
    session.add_all(default_tasks)
    await session.commit()
    print("--- Datos insertados y confirmados exitosamente. ---")


# --- FUNCIÓN PRINCIPAL DE EJECUCIÓN ---

async def main():
    print("--- Proceso de inicialización de Base de Datos iniciado ---")
    
    # 1. Crear las tablas si no existen
    async with engine.begin() as conn:
        print("Creando tablas (users, tasks) si no existen...")
        await conn.run_sync(Base.metadata.create_all)
    
    # 2. Conexión para inserción de datos
    async with AsyncSessionLocal() as session:
        # Verificar si ya hay datos
        user_count = await session.scalar(select(User.id).limit(1))
        
        if user_count is None:
            print("La tabla 'users' está vacía. Procediendo a poblar...")
            await populate_data(session)
        else:
            print("La tabla 'users' ya tiene registros. Omitiendo la inserción masiva.")
            print("Si desea forzar la reinserción, elimine el archivo db_muebles.db.")


if __name__ == "__main__":
    # Ejecuta la función principal
    asyncio.run(main())