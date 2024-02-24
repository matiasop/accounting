from typing import Literal

from pydantic import BaseModel, ConfigDict


class AccountDTO(BaseModel):
    id: int
    name: str
    type: Literal["ASSET", "LIABILITY"]
    initial_amount: int
    total: int
    model_config = ConfigDict(from_attributes=True)


class AccountInputDTO(BaseModel):
    """DTO for creating new Account"""

    name: str
    type: Literal["ASSET", "LIABILITY"]
    initial_amount: int
