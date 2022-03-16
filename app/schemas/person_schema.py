from sqlmodel import SQLModel


class PersonBaseSchema(SQLModel):
    name: str
    surname: str


class PersonCreateSchema(PersonBaseSchema):
    pass
