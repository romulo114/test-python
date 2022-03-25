from fastapi import FastAPI
from settings import API_VERSION, APP_DESC, APP_TITLE, DEBUG


def create_app():
    api_meta = [
        {
            'name': 'invoice',
            'description': 'Endpoints for invoice management'
        },
        {
            'name': 'system',
            'description': 'System information'
        }
    ]

    app = FastAPI(
        title=APP_TITLE,
        description=APP_DESC,
        version=API_VERSION,
        debug=DEBUG,
        openapi_tags=api_meta
    )

    return app
