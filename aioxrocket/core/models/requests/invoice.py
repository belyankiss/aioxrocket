from typing import Annotated, Optional

from pydantic import BaseModel, Field, HttpUrl

from aioxrocket.core.models.enums.currencies import CurrencyCodes


class InvoiceData(BaseModel):
   amount: Annotated[float, Field(ge=0)] = Field(ge=0, lt=1_000_000)
   currency: str = Field(default=CurrencyCodes.USDT)
   min_payment: Annotated[float, Field(default=0)] = Field(alias="minPayment", ge=0, default=0, lt=1_000_000)
   num_payments: Annotated[int, Field(default=1)] = Field(alias="numPayments", default=0, ge=0, lt=1_000_000)
   description: Optional[str] = Field(default="", max_length=1000)
   hidden_message: Optional[str] = Field(default="", max_length=2000)
   comments_enabled: bool = Field(default=False)
   callback_url: Optional[HttpUrl] = Field(default=None, max_length=500)
   payload: Optional[str] = Field(default="", max_length=4000)
   expired_in: Annotated[int, Field(default=0)] = Field(default=0, ge=0, lt=86400)


if __name__ == '__main__':
    i = InvoiceData(amount=12)
    print(i.model_dump(by_alias=True))