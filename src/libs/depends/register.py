from apps.invoice.libs.database.invoice import InvoiceDB
from apps.invoice.libs.database.invoice_item import InvoiceItemDB
from libs.database.base import DBEngine
from .entry import repo, DIEntry

def register_all():
    '''Register all DI entries'''

    register_database_engines()


def register_database_engines():

    def db_engine_create():
        return DBEngine()

    repo.add(DIEntry(
        DBEngine, db_engine_create
    ))

    def invoice_db_create():
        engine = repo.get(DBEngine)

        return InvoiceDB(engine)

    repo.add(DIEntry(
        InvoiceDB, invoice_db_create
    ))

    def invoice_item_db_create():
        engine = repo.get(DBEngine)

        return InvoiceItemDB(engine)

    repo.add(DIEntry(
        InvoiceItemDB, invoice_item_db_create
    ))

