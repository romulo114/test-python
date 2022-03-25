from typing import List
from apps.invoice.libs.database.invoice_item import InvoiceItemDB
from apps.invoice.libs.database.invoice import InvoiceDB
from .models import Invoice, InvoiceItem
from libs.depends.entry import repo

class InvoiceView:

    def __init__(self):
        self.invoice_db: InvoiceDB = repo.get(InvoiceDB)
        self.invoice_item_db: InvoiceItemDB = repo.get(InvoiceItemDB)


    async def get_all_invoices(self):

        invoices: List[Invoice] = await self.invoice_db.get_all()
        return {
            'count': len(invoices),
            'data': [obj.as_summary() for obj in invoices]
        }


    async def get_invoice(self, id: int):
        invoice: Invoice = await self.invoice_db.get_one(id)
        return { 'data': invoice.as_dict() }


    async def create_invoice(self):

        invoice: Invoice = await self.invoice_db.create()
        return { 'data': invoice.as_dict() }


    async def create_item(self, invoice_id: int, units: int, amount: float, description: str):
        invoice_item: InvoiceItem = await self.invoice_item_db.create(invoice_id, units, amount, description)
        return { 'data': invoice_item.as_dict() }
