from fastapi import FastAPI
from settings import API_VERSION, APP_DESC, APP_TITLE, DEBUG


def create_app():
    app = FastAPI(
        title=APP_TITLE,
        description=APP_DESC,
        version=API_VERSION,
        debug=DEBUG
    )

    return app
