from datetime import datetime
from enum import Enum

from pydantic import BaseModel, constr


class Type(str, Enum):
    ASSET = "ASSET"
    LIABILITY = "LIABILITY"
    TRANSFER = "TRANSFER"


class Category(str, Enum):
    FOOD = "FOOD"
    TRANSPORT = "TRANSPORT"
    DWELLING = "DWELLING"


class EntryDTO(BaseModel):
    id: int
    description: str
    # type: Type
    type: str
    datetime: datetime
    # category: Category
    category: str
    subcategory: str
    debit: int
    credit: int
    debit_account_id: int
    credit_account_id: int


class EntryInputDTO(BaseModel):
    """DTO for creating new entry"""

    description: constr(max_length=200)
    # type: Type
    type: str
    datetime: datetime
    # category: Category
    category: str
    subcategory: constr(max_length=200)
    debit: int
    credit: int
    debit_account_id: int
    credit_account_id: int
