from datetime import datetime
from sqlalchemy import TIMESTAMP, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship, Mapped
from database import Base


class Post(Base):
    __tablename__: str = "post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    test: Mapped[str] = mapped_column(String)
    topic: Mapped[str] = mapped_column(String)


class Users(Base):
    __tablename__: str = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    country: Mapped[str] = mapped_column(String)
    os: Mapped[str] = mapped_column(String)
    exp_group: Mapped[int] = mapped_column(Integer)


class FeedAction(Base):
    __tablename__: str = "feed_action"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), primary_key=True
    )
    user_relationship: Mapped["Users"] = relationship("Users")

    post_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("post.id"), primary_key=True
    )
    post_relationship: Mapped["Post"] = relationship("Post")

    action: Mapped[str] = mapped_column(String)
    time: Mapped[datetime] = mapped_column(TIMESTAMP)
