from typing import Optional, List

from pydantic import BaseModel, Field, conint, field_validator

from aioxrocket.core.models.enums import CountryCode


class MultiChequeData(BaseModel):
    currency: str
    chequePerUser: float = Field(
        gt=0,
        description="Cheque amount for one user. Max 9 decimal places"
    )
    usersNumber: conint(gt=0) = Field(
        description="Number of users to save multicheque. Integer only"
    )
    refProgram: conint(ge=0, le=100) = Field(
        description="Referral program percentage (0-100)"
    )
    password: Optional[str] = Field(
        default=None, max_length=100, description="Password for cheque"
    )
    description: Optional[str] = Field(
        default=None, max_length=1000, description="Description for cheque"
    )
    sendNotifications: bool = Field(
        default=True, description="Send notifications about activations"
    )
    enableCaptcha: bool = Field(
        default=True, description="Enable captcha"
    )
    telegramResourcesIds: List[str] = Field(
        default=[],
        description="IDs of telegram resources (groups, channels, private groups)",
        examples=["-1001799549067"]
    )
    forPremium: bool = Field(
        default=False, description="Only users with Telegram Premium can activate this cheque"
    )
    linkedWallet: bool = Field(
        default=False, description="Only users with linked wallet can activate this cheque"
    )
    disabledLanguages: List[str] = Field(
        default=[], description="Disable languages", examples=["NL", "FR"]
    )
    enabledCountries: List[CountryCode] = Field(
        default=[], description="Enabled countries", examples=[CountryCode.AD, CountryCode.AM]
    )


    @field_validator("chequePerUser", mode="before")
    @classmethod
    def validate_decimal_places(cls, v):
        as_str = f"{v:.9f}".rstrip("0").rstrip(".")
        return float(as_str)


