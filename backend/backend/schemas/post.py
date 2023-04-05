from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel
from backend.schemas.user import FilteredUserResponse


class PostBaseSchema(BaseModel):
    title: str
    content: str
    category: str
    image: str
    user_id: uuid.UUID or None = None

    class Config:
        orm_mode = True


class CreatePostSchema(PostBaseSchema):
    pass


class PostResponse(PostBaseSchema):
    id: uuid.UUID
    user: FilteredUserResponse
    created_at: datetime
    updated_at: datetime


class UpdatePostSchema(BaseModel):
    title: str
    content: str
    category: str
    image: str
    user_id: uuid.UUID or None = None
    created_at: datetime or None = None
    updated_at: datetime or None = None

    class Config:
        orm_mode = True


class ListPostResponse(BaseModel):
    status: str
    results: int
    posts: List[PostResponse]
