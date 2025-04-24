from typing import Literal

from aioxrocket.core.models import Version, App
from aioxrocket.core.models.requests.multi_cheque import MultiChequeData
from aioxrocket.core.session.base import BaseSession


class AioXRocket(BaseSession):
    def __init__(
            self,
            api_key: str,
            action: Literal["pay", "trade"] = "pay",
    ):
        self.api_key = api_key
        self.action = action
        super().__init__()

    async def version(self) -> Version:
        return Version(**await self.request(method="get", endpoint="version"))

    async def app(self) -> App:
        return App(**await self.request(method="get", endpoint="app/info"))

    async def multi_cheque(self, data: MultiChequeData):
        return await self.request(method="post", endpoint="multi-cheque", json=data.model_dump())


    def __repr__(self):
        return f"{self.api_key}, {self.url}"

