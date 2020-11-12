from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Date(models.Model):
    id = fields.IntField(pk=True)
    date = fields.DateField(unique=True)
    prices: fields.ReverseRelation["PriceItem"]


class PriceItem(models.Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(max_length=128)
    rate = fields.FloatField()
    date: fields.ForeignKeyRelation[Date] = fields.ForeignKeyField("models.Date", related_name="prices")


PriceItem_Pydantic = pydantic_model_creator(PriceItem, name="PriceItem")
Date_Pydantic = pydantic_model_creator(Date, name="Date")
