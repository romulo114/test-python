from fastapi import APIRouter, Request, Path, Form
from fastapi.responses import JSONResponse

from .libs.params import InvoiceItemParam
from .views import InvoiceView


router = APIRouter(prefix='/invoices')
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
    '''Get all invoices'''

    return await view.get_all_invoices()


@router.post(
    '',
    response_class=JSONResponse,
    summary='New invoice',
    description='Create a new invoice'
)
async def create(
    request: Request
):
    '''Create a new invoice'''

    return await view.create_invoice()


@router.get(
    '/{invoice_id}',
    response_class=JSONResponse,
    summary='An invoice',
    description='Get an invoice'
)
async def get_invoice(
    request: Request,
    invoice_id: int = Path(..., description='Invoice id')
):
    '''Get all invoices'''

    return await view.get_invoice(invoice_id)


@router.post(
    '/{invoice_id}/items',
    response_class=JSONResponse,
    summary='New invoice item',
    description='Create a new invoice item'
)
async def create_item(
    request: Request,
    param: InvoiceItemParam,
    invoice_id: int = Path(..., description='Invoice id which new items belongs to'),
):
    '''Create a new invoice item for an invoice'''

    return await view.create_item(invoice_id, param.units, param.amount, param.description)
