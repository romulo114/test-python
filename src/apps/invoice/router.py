from fastapi import APIRouter, Depends, Request, Path, Query
from fastapi.responses import JSONResponse
from .libs.params import InvoiceItemParam, UpdateItemPayload
from .views import InvoiceView


router = APIRouter(prefix='/invoices')
view = InvoiceView()

@router.get(
    '',
    response_class=JSONResponse,
    summary='All invoices',
    description='Get all invoices',
    tags=['invoice']
)
async def get_all(
    request: Request,
    page: int = Query(1, description='Page number'),
    page_size: int = Query(10, description='Page size')
):
    '''Get all invoices'''

    return await view.get_all_invoices(page, page_size)


@router.post(
    '',
    response_class=JSONResponse,
    summary='New invoice',
    description='Create a new invoice',
    tags=['invoice']
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
    description='Get an invoice',
    tags=['invoice']
)
async def get_invoice(
    request: Request,
    invoice_id: int = Path(..., description='Invoice id')
):
    '''Get an invoice'''

    return await view.get_invoice(invoice_id)


@router.delete(
    '/{invoice_id}',
    response_class=JSONResponse,
    summary='Delete an invoice',
    tags=['invoice']
)
async def delete_invoice(
    request: Request,
    invoice_id: int = Path(..., description='Invoice id to delete')
):
    '''Delete an invoice'''

    return await view.delete_invoice(invoice_id)


@router.post(
    '/{invoice_id}/items',
    response_class=JSONResponse,
    summary='New invoice item',
    description='Create a new invoice item',
    tags=['invoice']
)
async def create_item(
    request: Request,
    param: InvoiceItemParam,
    invoice_id: int = Path(..., description='Invoice id which new items belongs to'),
):
    '''Create a new invoice item for an invoice'''

    return await view.create_item(invoice_id, param.units, param.amount, param.description)


@router.put(
    '/items/{id}',
    summary='Update an invoice item',
    tags=['invoice']
)
async def update_item(
    request: Request,
    payload: UpdateItemPayload,
    id: int = Path(..., description='Invoice item id to update')
):
    '''Update an invoice item'''

    params = payload.normalize()
    return await view.update_item(id, **params)


@router.delete(
    '/items/{id}',
    summary='Delete an invoice item',
    tags=['invoice']
)
async def delete_item(
    request: Request,
    id: int = Path(..., description='Invoice item id to delete')
):
    '''Delete an invoice item'''

    return await view.delete_item(id)
