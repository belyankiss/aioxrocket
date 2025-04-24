from typing import List

from pydantic import BaseModel, Field

from aioxrocket.core.models.responses.base_model import Base

class Coins(BaseModel):
    currency: str
    balance: float

class AppData(BaseModel):
    name: str
    fee_percents: float = Field(alias="feePercents")
    balances: List[Coins]


class App(Base):
    data: AppData