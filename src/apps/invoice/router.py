from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from .views import InvoiceView


router = APIRouter()
view = InvoiceView()

@router.get(
    '',
    response_class=JSONResponse,
    summary='All invoices',
    description='Get all invoices'
)
async def get_all(
    request: Request
):
    return await view.get_all()


@router.post(
    '',
    response_class=JSONResponse,
    summary='New invoice',
    description='Create a new invoice'
)
async def create(
    request: Request
):
    return await view.create()
