from typing import List, Optional

from pydantic import BaseModel, Field


class ErrorProperty(BaseModel):
    field: str = Field(alias="property")
    error: str

class XRocketExceptionModel(BaseModel):
    success: bool
    message: str
    errors: Optional[List[ErrorProperty]] = None

class XRocketException(Exception):
    def __init__(self, error: XRocketExceptionModel):
        self.error = error