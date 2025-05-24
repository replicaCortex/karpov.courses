from sqlalchemy import ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import mapped_column, relationship, Mapped
from .database import Base
from datetime import datetime


class Post(Base):
    __tablename__: str = "post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String)
    topic: Mapped[str] = mapped_column(String)


class Users(Base):
    __tablename__: str = "user_data"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    gender: Mapped[int] = mapped_column(Integer)
    age: Mapped[int] = mapped_column(Integer)
    country: Mapped[str] = mapped_column(String)
    os: Mapped[str] = mapped_column(String)
    exp_group: Mapped[int] = mapped_column(Integer)


class FeedAction(Base):
    __tablename__: str = "feed_data"

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user_data.user_id"), primary_key=True
    )
    user_relationship: Mapped["Users"] = relationship("Users")

    post_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("post.id"), primary_key=True
    )
    post_relationship: Mapped["Post"] = relationship("Post")

    action: Mapped[str] = mapped_column(String)
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP)
