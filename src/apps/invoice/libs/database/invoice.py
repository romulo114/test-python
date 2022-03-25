from libs.database.base import DBEngine
from apps.invoice.models import Invoice

class InvoiceDB:
	
	def __init__(self, engine: DBEngine):
		self.engine = engine


	async def get_all(self, page: int, page_size: int):
		return await self.engine.get_all(Invoice, page, page_size)


	async def get_one(self, id: int):
		return await self.engine.get_one(Invoice, id)


	async def create(self):
		return await self.engine.create_one(Invoice)


	async def delete(self, id: int):
		return await self.engine.delete_one(Invoice, id)
