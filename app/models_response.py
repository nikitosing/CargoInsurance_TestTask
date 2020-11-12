import datetime

from pydantic import BaseModel
from pydantic.class_validators import List


class ResponseCost(BaseModel):
    cost: float


class ResponseStatus(BaseModel):
    message: str


class ResponsePriceItem(BaseModel):
    cargo_type: str
    rate: float


class PriceForPush(BaseModel):
    date: datetime.date
    items: List[ResponsePriceItem]
