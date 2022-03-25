from libs.database import init_db

async def startup():
    await init_db()


async def shutdown():
    pass
