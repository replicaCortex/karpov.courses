from datetime import datetime
from pydantic import BaseModel


class UserGet(BaseModel):
    user_id: int
    gender: int
    age: int
    country: str = ""
    os: str = ""
    exp_group: int

    class Config:
        from_attributes: bool = True


class PostGet(BaseModel):
    id: int
    text: str = ""
    topic: str = ""

    class Config:
        from_attributes: bool = True


class FeedActionGet(BaseModel):
    user_id: int
    user_relationship: UserGet

    post_id: int
    post_relationship: PostGet

    timestamp: datetime
    action: str = ""

    class Config:
        from_attributes: bool = True
