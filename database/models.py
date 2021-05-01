from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime as dt

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, BigInteger, Text, Table, DateTime


"""
Продолжить работу с парсером блога GB
Реализовать SQL базу данных посредствам SQLAlchemy
Реализовать реалиционные связи между Постом и Автором, Постом и Тегом, Постом и комментарием, Комментарием и комментарием
"""
Base = declarative_base()

tag_post = Table(
    "tag_post",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("post.id")),
    Column("tag_id", Integer, ForeignKey("tag.id")),
)


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, unique=True, nullable=False)
    title = Column(String(250), nullable=False, unique=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=True)
    author = relationship("Author", backref="posts")
    tags = relationship("Tag", secondary=tag_post, backref="posts")


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, unique=True, nullable=False)
    name = Column(String(150), nullable=False)


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, unique=True, nullable=False)
    name = Column(String(150), nullable=False)





