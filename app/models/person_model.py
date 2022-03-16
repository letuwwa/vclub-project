from sqlmodel import Field

from app.models.base_model import Base
from app.schemas import PersonBaseSchema


class Person(PersonBaseSchema, Base, table=True):
    name: str = Field(index=False)
    surname: str = Field(index=False)
