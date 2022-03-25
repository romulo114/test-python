from libs.database.base import DBEngine
from apps.invoice.models import Invoice

class InvoiceDB:
	
	def __init__(self, engine: DBEngine):
		self.engine = engine


	async def get_all(self):
		return await self.engine.get_all(Invoice)


	async def get_one(self, id: str):
		return await self.engine.get_one(Invoice, id)


	async def create(self):
		return await self.engine.create_one(Invoice)
