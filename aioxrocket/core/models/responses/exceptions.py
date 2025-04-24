from typing import List

from pydantic import BaseModel, Field


class ErrorProperty(BaseModel):
    field: str = Field(alias="property")
    error: str

class XRocketExceptionModel(BaseModel):
    success: bool
    message: str
    errors: List[ErrorProperty]

class XRocketException(Exception):
    def __init__(self, error: XRocketExceptionModel):
        self.error = error