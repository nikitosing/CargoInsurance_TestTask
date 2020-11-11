from pydantic import BaseModel
import datetime
from models import PriceItem_Pydantic
from pydantic.class_validators import List


class ResponseCost(BaseModel):
    cost: float


class ResponseStatus(BaseModel):
    message: str


class PriceItem__(BaseModel):
    cargo_type: str
    rate: float


class PriceForPush(BaseModel):
    date: datetime.date
    items: List[PriceItem__]
