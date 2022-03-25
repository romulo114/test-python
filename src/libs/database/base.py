from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select, delete, update
from sqlalchemy.engine import CursorResult
from libs.database import db_session


class DBEngine:

    def __init__(self):
        self.session: sessionmaker = db_session


    async def get_all(self, modelClass, page: int, page_size: int) -> List:
        query = select(modelClass).offset((page - 1) * page_size).limit(page_size)
        count_query = select([func.count()]).select_from(modelClass)
        session: AsyncSession

        async with self.session() as session:
            async with session.begin():
                result = await session.execute(query)
                count = await session.execute(count_query)
                await session.flush()

                return (count.scalar(), result.scalars().unique().all())


    async def get_one(self, modelClass, id: int):
        query = select(modelClass).where(modelClass.id == id)
        session: AsyncSession

        async with self.session() as session:
            async with session.begin():
                result: CursorResult = await session.execute(query)
                await session.flush()
                return result.scalar()


    async def exec_query(self, query):
        session: AsyncSession

        async with self.session() as session:
            async with session.begin():
                result: CursorResult = await session.execute(query)
                await session.flush()
                return result.scalars().unique().all()


    async def create_one(self, modelClass, **kwargs):
        session: AsyncSession

        instance = modelClass(**kwargs)
        async with self.session() as session:
            async with session.begin():
                session.add(instance)
                await session.flush()

                query = select(modelClass).where(modelClass.id == instance.id)
                result: CursorResult = await session.execute(query)
                await session.flush()
                return result.scalars().unique().one()


    async def update_one(self, modelClass, id: int, **kwargs):
        query = update(modelClass).where(modelClass.id == id).values(**kwargs)
        fetch_query = select(modelClass).where(modelClass.id == id)
        session: AsyncSession

        async with self.session() as session:
            async with session.begin():
                await session.execute(query)
                result: CursorResult = await session.execute(fetch_query)
                await session.flush()
                return result.scalar()


    async def delete_one(self, modelClass, id: int):
        query = delete(modelClass).where(modelClass.id == id)
        session: AsyncSession

        async with self.session() as session:
            async with session.begin():
                await session.execute(query)
                await session.flush()
