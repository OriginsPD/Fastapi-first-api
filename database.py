from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

# SQLALCHEMY_DATABASE_URL = "sqlite:///blog.sqlite3"

DB_USER: str = "postgres"
DB_NAME: str = "Fastapi"
DB_PASS: str = "MADman123"
PORT: int = 5432

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@localhost:{PORT}/{DB_NAME}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
