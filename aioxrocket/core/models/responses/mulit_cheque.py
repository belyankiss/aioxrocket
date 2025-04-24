from typing import List, Optional, Union

from pydantic import BaseModel, HttpUrl, Field

from aioxrocket.core.models.enums import CountryCode
from aioxrocket.core.models.requests.multi_cheque import MultiChequeData
from aioxrocket.core.models.responses.base_model import Base

class UserMultiCheque(BaseModel):
    total: int
    limit: int
    offset: int
    results: List[MultiChequeData]

class MultiChequeResult(Base):
    data: UserMultiCheque

class TGResource(BaseModel):
    telegramId: Union[str, int]
    name: str
    username: str

class ExistCheque(MultiChequeData):
    refProgramPercents: Optional[int]
    refRewardPerUser: Optional[float]
    state: str
    link: HttpUrl
    forNewUsersOnly: Optional[int] = Field(default=0)
    linkedWallet: Optional[int] = Field(default=0)
    tgResources: List[TGResource]
    activations: int
    refRewards: int

class CreatedMultiCheque(Base):
    data: ExistCheque


class EditMultiChequeData(BaseModel):
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
