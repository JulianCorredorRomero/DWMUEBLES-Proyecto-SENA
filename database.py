# database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.future import select
from sqlalchemy import text 

DATABASE_URL = "sqlite+aiosqlite:///./db_muebles.db"

engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)      # 'Cliente', 'Carpintero', 'Administrador'

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    status = Column(String, default="Pendiente") # Ej: Pendiente, En Progreso, Finalizada
    carpenter_assigned = Column(String, nullable=True) # Nombre del carpintero asignado
    is_urgent = Column(Boolean, default=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
        session = AsyncSessionLocal(bind=conn)
        
        user_count_query = await session.scalar(select(User.id).limit(1))
        
        if user_count_query is None: # Si no encuentra ningún ID, significa que está vacía
            default_users = [
                User(username="juan", password="1234", role="Cliente"),
                User(username="maria", password="5678", role="Carpintero"),
                User(username="admin", password="admin123", role="Administrador"),
            ]
            default_tasks = [
                Task(title="Reparación de Mesa", description="Arreglar pata rota en mesa de comedor.", status="Pendiente", carpenter_assigned="maria"),
                Task(title="Diseño de Gabinetes", description="Crear gabinetes a medida para cocina principal.", status="En Progreso", carpenter_assigned="maria", is_urgent=True),
            ]
            session.add_all(default_users)
            session.add_all(default_tasks)
            
            await session.commit()
            
        await session.close()
