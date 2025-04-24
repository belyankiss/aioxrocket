from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class XRocketAPIServer:
    base: str

    def api_url(self, endpoint: str):
        return self.base.format(endpoint=endpoint)

    @classmethod
    def headers(cls, method: Literal["pay", "trade"], api_key: str):
        if method == "pay":
            return {'Rocket-Pay-Key': api_key}
        return {'Rocket-Exchange-Key': api_key}

PRODUCTION = XRocketAPIServer(
    base="https://pay.xrocket.tg/{endpoint}"
)
