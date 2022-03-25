from typing import List
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from libs.database import db_session


class DBEngine:

    def __init__(self):
        self.session: sessionmaker = db_session


    async def get_all(self, modelClass) -> List:
        query = select(modelClass)
        session: AsyncSession

        async with self.session() as session:
            async with session.begin():
                result = await session.execute(query)
                await session.flush()
                return result.scalars().unique().all()


    async def get_one(self, modelClass, id: str):
        query = select(modelClass).where(modelClass.id == id)
        session: AsyncSession

        async with self.session() as session:
            async with session.begin():
                result = await session.execute(query)
                await session.flush()
                return result.scalars().unique().one()


    async def create_one(self, modelClass, **kwargs):
        session: AsyncSession

        instance = modelClass(**kwargs)
        async with self.session() as session:
            async with session.begin():
                session.add(instance)
                await session.flush()

                query = select(modelClass).where(modelClass.id == instance.id)
                result = await session.execute(query)
                await session.flush()
                return result.scalars().unique().one()
