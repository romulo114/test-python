from sqlalchemy.ext.asyncio import AsyncConnection
from . import db_session

async def default_values(connection: AsyncConnection):
    '''Populate default values'''
    pass
