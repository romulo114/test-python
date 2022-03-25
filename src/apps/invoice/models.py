from libs.database import Base
from sqlalchemy import (
    Column,
    Numeric,
    ForeignKey,
    Integer,
    String,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, server_default=func.now())

    items = relationship('InvoiceItem', back_populates='invoice', lazy='joined', cascade='all, delete, delete-orphan')


    def as_dict(self):
        return {
            'id': self.id,
            'created_date': self.created_date,
            'items': self.items
        }


    def as_summary(self):
        return {
            'id': self.id,
            'created_date': self.created_date
        }


class InvoiceItem(Base):
    __tablename__ = 'invoice_items'

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id', ondelete="CASCADE"), nullable=False)
    units = Column(Integer, nullable=False)
    amount = Column(Numeric, nullable=False)
    description = Column(String, default='')

    invoice = relationship('Invoice', back_populates='items')


    def as_dict(self):
        return {
            'id': self.id,
            'units': self.units,
            'amount': self.amount,
            'description': self.description
        }
