from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import true

# engine =create_engine('sqlite:///:memory:', echo= True)

SQL_ALCHEMY_DATA_BASE_URL= 'sqlite:///./blog.db'
engine = create_engine(
    SQL_ALCHEMY_DATA_BASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker( bind=engine,autocommit=False, autoflush=False)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 