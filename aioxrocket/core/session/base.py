import logging
from typing import List

from aiohttp import ClientSession
from pydantic import ValidationError
from typing_extensions import Literal

from aioxrocket.core.models.responses.exceptions import XRocketExceptionModel, ErrorProperty, XRocketException
from aioxrocket.core.session.xrocket import PRODUCTION


class BaseSession:

    action: str
    api_key: str

    def __init__(self):
        self.url = PRODUCTION

    async def request(self, method: Literal["get", "post", "put", "delete"], endpoint: str, **kwargs):
        url = self.url.api_url(endpoint)
        async with ClientSession() as session:
            async with getattr(session, method)(
                    url=url,
                    headers=self.url.headers(method=self.action, api_key=self.api_key),
                    **kwargs) as response:
                r = await response.json()
                print(r)
                try:
                    error = XRocketExceptionModel(**r)
                    all_errors: List[ErrorProperty] = error.errors
                    if not error.success:
                        if error.errors:
                            logging.error(msg=f"{"\n".join([str(err.error) for err in all_errors])}")
                        else:
                            logging.error(msg=f"{error.message}")
                        raise XRocketException(error)
                    return None
                except ValidationError:
                    response.raise_for_status()
                    return r


