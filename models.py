from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine

DB_CONNECTION = "postgresql+psycopg2://postgres@localhost:5432/postgres"
engine = create_engine(DB_CONNECTION, echo=False)

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username  = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")

Base.metadata.create_all(bind=engine)

