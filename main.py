from uuid import UUID

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.managers import PersonManager
from app.models import Person
from app.schemas import PersonCreateSchema
from settings import get_session

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/person/{person_id}", response_model=Person)
async def get_person(person_id: UUID, session: AsyncSession = Depends(get_session)):
    return await PersonManager(session).get_by_id(uuid=person_id)


@app.post("/person", response_model=Person)
async def post_person(person: PersonCreateSchema, session: AsyncSession = Depends(get_session)):
    return await PersonManager(session).post(item=person)

if __name__ == "__main__":
    uvicorn.run(app=app)
