from .app import create_app
from .router import register_routes
from libs.server import startup, shutdown
from libs.depends.register import register_all

register_all()
app = create_app()
register_routes(app)


@app.on_event('startup')
async def on_startup():
    await startup()


@app.on_event('shutdown')
async def on_shutdown():
    await shutdown()
