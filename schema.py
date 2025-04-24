from datetime import datetime
from pydantic import BaseModel


class UserGet(BaseModel):
    id: int
    country: str = ""
    os: str = ""
    exp_group: int

    class Config:
        from_attributes: bool = True


class PostGet(BaseModel):
    id: int
    test: str = ""
    topic: str = ""

    class Config:
        from_attributes: bool = True


class FeedActionGet(BaseModel):
    id: int

    user_id: int
    user_relationship: UserGet

    post_id: int
    post_relationship: PostGet

    time: datetime
    action: str = ""

    class Config:
        from_attributes: bool = True
