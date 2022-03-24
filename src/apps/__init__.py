from fastapi import FastAPI
from settings import API_VERSION, APP_DESC, APP_TITLE, DEBUG
from libs.server import startup, shutdown
from apps.invoice.router import router as invoice_router

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESC,
    version=API_VERSION,
    debug=DEBUG
)

@app.get('/healthy')
def check_healthy():
    return 'Service is running'


app.include_router(router=invoice_router, prefix='/invoice')


@app.on_event('startup')
async def on_startup():
    await startup()


@app.on_event('shutdown')
async def on_shutdown():
    await shutdown()
