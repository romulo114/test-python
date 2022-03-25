from fastapi import FastAPI
from settings import API_VERSION


def register_routes(app: FastAPI):
    @app.get('/api/healthy')
    def check_healthy():
        return 'Service is running'

    from apps.invoice.router import router as invoice_router
    app.include_router(router=invoice_router, prefix=f'/api/{API_VERSION}')
