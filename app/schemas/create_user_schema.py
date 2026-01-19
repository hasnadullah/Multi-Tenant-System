from pydantic import BaseModel
from typing import Literal

class CreateUserSchema(BaseModel):
    email: str
    password: str
    role: Literal["manager", "viewer"]
