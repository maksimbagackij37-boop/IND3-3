from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Dish(BaseModel):
    id: int
    name: str = Field(..., example="Борщ")
    category: str = Field(..., example="Супи")
    price: int = Field(..., gt=0, example=75)
    emoji: str = Field(..., example="🍲")


class OrderCreate(BaseModel):
    dish_ids: list[int] = Field(..., min_length=1, example=[1, 3])


class Order(BaseModel):
    id: int
    dishes: list[Dish]
    total: int
    created_at: datetime


class ErrorResponse(BaseModel):
    detail: str = Field(..., example="Страву з ID 99 не знайдено")
