from this import d
from typing import Optional
from pydantic import BaseModel, Field

class InvoiceItemParam(BaseModel):
    units: int = Field(..., title='Payment unit of the invoice')
    amount: float = Field(..., title='Amount')
    description: Optional[str] = Field(None, title='Invoice description')


class UpdateItemPayload(BaseModel):
    units: Optional[int] = Field(None, title='Payment unit of the invoice')
    amount: Optional[float] = Field(None, title='Amount')
    description: Optional[str] = Field(None, title='Invoice description')

    def normalize(self):
        param = {}
        for key in self.__dict__:
            if self.__dict__[key] is not None:
                param[key] = self.__dict__[key]

        return param
