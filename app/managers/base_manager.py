from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID


class BaseManager:
    def __init__(self, session: AsyncSession):
        self.session = session

    model = None

    async def post(self, item: SQLModel):
        item = self.model(**item.dict(exclude_none=True))
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

    async def get_by_id(self, uuid: UUID):
        item = await self.session.get(self.model, uuid)
        if not item:
            return {}
        return item

    def put(self):
        pass

    def delete(self):
        pass
