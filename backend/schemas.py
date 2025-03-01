from pydantic import BaseModel, ConfigDict

class BookSchema(BaseModel):
    title: str
    author: str

class BookGetSchema(BaseModel):
    id: int
    title: str
    author: str

    model_config = ConfigDict(from_attributes=True)