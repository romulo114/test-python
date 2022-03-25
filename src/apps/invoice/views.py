from apps.invoice.libs.database.invoice_item import InvoiceItemDB
from apps.invoice.libs.database.invoice import InvoiceDB
from .models import Invoice, InvoiceItem
from libs.depends.entry import repo

class InvoiceView:

    def __init__(self):
        self.invoice_db: InvoiceDB = repo.get(InvoiceDB)
        self.invoice_item_db: InvoiceItemDB = repo.get(InvoiceItemDB)


    async def get_all_invoices(self, page: int, page_size: int):
        count, invoices = await self.invoice_db.get_all(page, page_size)
        return {
            'total': count,
            'data': [obj.as_summary() for obj in invoices]
        }


    async def get_invoice(self, id: int):
        invoice: Invoice = await self.invoice_db.get_one(id)
        return { 'data': invoice.as_dict() if invoice else None }


    async def delete_invoice(self, id: int):
        await self.invoice_db.delete(id)
        return { 'result': 'success' }


    async def create_invoice(self):

        invoice: Invoice = await self.invoice_db.create()
        return { 'data': invoice.as_dict() }


    async def create_item(self, invoice_id: int, units: int, amount: float, description: str):
        item: InvoiceItem = await self.invoice_item_db.create(invoice_id, units, amount, description)
        return { 'data': item.as_dict() }


    async def update_item(self, id: int, **kwargs):
        item: InvoiceItem = await self.invoice_item_db.update(id, **kwargs)
        return { 'data': item.as_dict() }


    async def delete_item(self, id: int):
        await self.invoice_item_db.delete(id)
        return { 'result': 'success' }
