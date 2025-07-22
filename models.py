from pydantic import BaseModel
from pydantic.dataclasses import Field, dataclass
import uuid

class Task(BaseModel):
    title: str
    description: str

@dataclass
class TaskModel():
    title: str = Field(default="", init=True, kw_only=True)
    description: str = Field(default="", init=True, kw_only=True)
    id: str = Field(default="", init=False)
    deleted: bool = Field(default=False, init=False)

    def __post_init__(self):
        self.id = str(uuid.uuid4())

class User(BaseModel):
    name: str
    password: str

@dataclass
class UserModel():
    name: str = Field(default="", init=True, kw_only=True)
    password: str = Field(default="", init=True, kw_only=True)
    id: str = Field(default="", init=False)
    deleted: bool = Field(default=False, init=False)

    def __post_init__(self):
        self.id = str(uuid.uuid4())