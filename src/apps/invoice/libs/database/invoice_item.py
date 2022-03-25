from libs.database.base import DBEngine
from apps.invoice.models import InvoiceItem

class InvoiceItemDB:
    
    def __init__(self, engine: DBEngine):
        self.engine = engine


    async def get_all(self):
        return await self.engine.get_all(InvoiceItem)


    async def get_one(self, id: str):
        return await self.engine.get_one(InvoiceItem, id)


    async def create(self, invoice_id: int, units: int, amount: float, description: str):
        return await self.engine.create_one(
            InvoiceItem,
            invoice_id=invoice_id,
            units=units,
            amount=amount,
            description=description
        )


    async def update(self, id: int, **kwargs):
        return await self.engine.update_one(InvoiceItem, id, **kwargs)


    async def delete(self, id: int):
        return await self.engine.delete_one(InvoiceItem, id)
