import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carga .env local
load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

# SQLite necesita connect_args, Postgres no
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# Sesión de DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de los modelos
Base = declarative_base()
