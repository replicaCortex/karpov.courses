from fastapi import Depends, FastAPI
from sqlalchemy import func
from sqlalchemy.orm import Session

from database import SessionLocal
from schema import PostGet, UserGet, FeedActionGet
from table_post import Users, Post, FeedAction

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get("/user/{id}", response_model=list[UserGet])
def get_user_id(id: int, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Users).filter(Users.id == id).limit(limit).all()


@app.get("/post/{id}", response_model=list[PostGet])
def get_post_id(id: int, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Post).filter(Post.id == id).limit(limit).all()


@app.get("/user/{id}/feed", response_model=list[FeedActionGet])
def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    return (
        db.query(FeedAction)
        .filter(FeedAction.user_id == id)
        .order_by(FeedAction.time.desc())
        .limit(limit)
        .all()
    )


@app.get("/post/{id}/feed", response_model=list[FeedActionGet])
def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):
    return (
        db.query(FeedAction)
        .filter(FeedAction.post_id == id)
        .order_by(FeedAction.time.desc())
        .limit(limit)
        .all()
    )


@app.get("/post/recommendations/", response_model=list[FeedActionGet])
def get_post_recommend(id: int = 3, limit: int = 10, db: Session = Depends(get_db)):
    return (
        db.query(
            FeedAction.post_id,
            func.count(FeedAction.post_id.label("Like count")),
        )
        # .filter(FeedAction.post_id == id)
        .where(FeedAction.action == "like")
        .group_by(FeedAction.post_id)
        # .order_by(func.count(FeedAction.post_id))
        .limit(limit)
        .all()
    )
