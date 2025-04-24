from typing import Any, Optional

from pydantic import BaseModel


class Base(BaseModel):
    success: bool
    data: Optional[Any] = None