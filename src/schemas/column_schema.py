from pydantic import BaseModel


class CreateColumn(BaseModel):
    title: str
