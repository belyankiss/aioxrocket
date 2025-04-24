from typing import List

from pydantic import BaseModel, Field

from aioxrocket.core.models.responses.base_model import Base

class CurrencyType(BaseModel):
    currency: str
    name: str
    min_transfer: float = Field(alias="minTransfer")
    min_cheque: float = Field(alias="minCheque")
    min_invoice: float = Field(alias="minInvoice")
    min_withdraw: float = Field(alias="minWithdraw")


class Currency(Base):
    data: dict[str, List[CurrencyType]]



