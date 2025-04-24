from typing import Any

from pydantic import BaseModel


class Base(BaseModel):
    success: bool
    data: Any