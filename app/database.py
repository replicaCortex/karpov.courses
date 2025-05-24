from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml"

# SQLALCHEMY_DATABASE_URL = "postgresql://postgresql:password@localhost:5432/post"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=True, bind=engine)

Base: type["DeclarativeBase"] = declarative_base()
