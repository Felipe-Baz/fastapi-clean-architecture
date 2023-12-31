from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import HttpUrl


class UserRequest(BaseModel):
    name: str = Field(min_length=3, max_length=64)
    email: EmailStr
    avatar: HttpUrl


class UserResponse(BaseModel):
    id: str
    name: str = Field(min_length=3, max_length=64)
    email: EmailStr
    avatar: HttpUrl

    class Config:
        from_attributes = True
        populate_by_name = True
