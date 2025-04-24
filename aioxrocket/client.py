from typing import Literal

from aioxrocket.core.models import Version, App
from aioxrocket.core.models.enums.currencies import CurrencyCodes
from aioxrocket.core.models.requests.invoice import InvoiceData
from aioxrocket.core.models.requests.multi_cheque import MultiChequeData
from aioxrocket.core.models.responses.base_model import Base
from aioxrocket.core.models.responses.currencies import Currency
from aioxrocket.core.models.responses.mulit_cheque import MultiChequeResult, CreatedMultiCheque, EditMultiChequeData
from aioxrocket.core.session.base import BaseSession
from aioxrocket.settings import TOKEN


class AioXRocket(BaseSession):
    def __init__(
            self,
            api_key: str,
            action: Literal["pay", "trade"] = "pay",
    ):
        self.api_key = api_key
        self.action = action
        super().__init__()

    async def version_xrocket(self) -> Version:
        return Version(**await self.request(method="get", endpoint="version"))

    async def app_info(self) -> App:
        return App(**await self.request(method="get", endpoint="app/info"))

    async def create_multi_cheque(self, data: MultiChequeData) -> CreatedMultiCheque:
        return CreatedMultiCheque(**await self.request(method="post", endpoint="multi-cheque", json=data.model_dump()))

    async def get_multi_cheque(self, limit: int = 100, offset: int = 0) -> MultiChequeResult:
        return MultiChequeResult(**await self.request(method="get",
                                                      endpoint=f"multi-cheque?limit={limit}&offset={offset}"))

    async def get_multi_cheque_id(self, id_cheque: int) -> CreatedMultiCheque:
        return CreatedMultiCheque(**await self.request(method="get", endpoint=f"multi-cheque/{id_cheque}"))

    async def edit_multi_cheque(self, id_cheque: int, data: EditMultiChequeData) -> CreatedMultiCheque:
        return CreatedMultiCheque(**await self.request(method="put",
                                                       endpoint=f"multi-cheque/{id_cheque}",
                                                       json=data.model_dump()))

    async def delete_multi_cheque(self, id_cheque: int) -> bool:
        return Base(**await self.request(method="delete", endpoint=f"multi-cheque/{id_cheque}")).success

    async def create_invoice(self, data: InvoiceData):
        await self.request(method="post", endpoint="tg-invoices", json=data.model_dump(by_alias=True))

    async def get_currencies(self):
        r = Currency(**await self.request(method="get", endpoint="currencies/available"))
        cur = r.data.get("results")
        for i in cur:
            print(f'{i.currency} = "{i.currency}"')


    def __repr__(self):
        return f"{self.api_key}, {self.url}"

if __name__ == '__main__':
    import asyncio
    a = AioXRocket(api_key=TOKEN)
    print(asyncio.run(a.create_invoice(InvoiceData(amount=5, currency=CurrencyCodes.USDT))))