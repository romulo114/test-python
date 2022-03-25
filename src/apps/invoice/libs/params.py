from this import d
from typing import Optional
from pydantic import BaseModel, Field

class InvoiceItemParam(BaseModel):
    units: int = Field(..., title='Payment unit of the invoice')
    amount: float = Field(..., title='Amount')
    description: Optional[str] = Field(None, title='Invoice description')