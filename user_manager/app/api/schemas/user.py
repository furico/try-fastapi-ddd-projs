from typing import Literal

from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    user_id: int
    email: EmailStr
    status: Literal["active", "banned"]
