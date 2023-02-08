import datetime

from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from models import *
from models_response import *
from pydantic.class_validators import List, Dict
from tortoise.contrib.fastapi import register_tortoise
from strings import example_push_price

app = FastAPI()


@app.put("/push_price", response_model=ResponseStatus)
async def push_price(price: Dict[(datetime.date, List[ResponsePriceItem])] = Body(..., example=example_push_price)):
    for date_key in price:
        date = (await Date.get_or_create(date=date_key))[0]
        for price_item in price[date_key]:
            item = await PriceItem.get_or_none(cargo_type=price_item.cargo_type, date_id=date.id)
            if item is None:
                item = PriceItem(cargo_type=price_item.cargo_type, date_id=date.id, rate=price_item.rate)
                await item.save()
            else:
                item.rate = price_item.rate
                await item.save()
    return ResponseStatus(message="success")


@app.get("/get_db", response_model=Dict[(datetime.date, List[PriceItem_Pydantic])])
async def return_db():
    response_dict = {}
    dates = await Date.all()
    for date in dates:
        response_dict[date.date] = await PriceItem.filter(date_id=date.id).all()
    return response_dict


@app.get("/get_cost", response_model=ResponseCost, responses={404: {"model": ResponseStatus}})
async def return_cost(declared_price: float, cargo_type: str, date: datetime.date):
    requested_date = await Date.get_or_none(date=date)
    if requested_date is None:
        return JSONResponse(status_code=404, content={"message": "date not found"})
    requested_cargo = await PriceItem.get_or_none(date_id=requested_date.id, cargo_type=cargo_type)
    if requested_cargo is None:
        return JSONResponse(status_code=404, content={"message": "cargo_type not found"})
    return ResponseCost(cost=requested_cargo.rate * declared_price)


register_tortoise(
    app,
    db_url="postgres://postgres:password@host.docker.internal:5432/postgres",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
