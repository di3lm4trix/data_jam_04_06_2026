from dataclasses import dataclass
from datetime import datetime

@dataclass
class Category:
    id: int
    slug: str
    name: str

@dataclass
class Products:
    id: int
    name: str
    price: float
    category_id: int

@dataclass
class ProductDetails:
    product_id: int
    stock: int
    rating: float
    weight: float

@dataclass
class OrderItems:
    id: int
    order_id: int
    product_id: int
    quantity: int
    unit_price: float

@dataclass
class Orders:
    id: int
    user_id: int
    order_date: datetime
    total_amount: float

@dataclass
class Users:
    id: int
    name: str
    email: str
    country_code: str
    created_at: datetime

@dataclass
class Country:
    code: str
    name: str
    region: str
    population: int = 0

@dataclass
class ShippingRegion:
    country_code: str
    region: str
    shipping_zone: str
    estimated_days: int

@dataclass
class CurrencyRate:
    currency_code: str
    rate_to_usd: float
    updated_at: datetime
