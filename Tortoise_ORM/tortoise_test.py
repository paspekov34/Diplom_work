from tortoise import fields
from tortoise.models import Model
from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix="/products", tags=["product"])


class Product(Model):
    id = fields.IntField(pk=True)
    product_name = fields.CharField(max_length=275)
    product_type = fields.CharField(max_length=275)
    product_description = fields.TextField()

    def __str__(self):
        return self.product_name

