import csv
from datetime import datetime
from models import Category, Country, Users, Products, ProductDetails, Orders, OrderItems, ShippingRegion

def read_categories_csv(path):
    categories = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            categories.append(
                Category(
                    id=int(row['id']),
                    slug=row['slug'],
                    name=row['name']
                )
            )
    return categories

def read_countries_csv(path):
    countries = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['code']:  # Only add if not empty
                countries.append(
                    Country(
                        code=row['code'],
                        name=row['name'],
                        region=row['region'],
                        population=int(row.get('population', 0)) if row.get('population') else 0
                    )
                )
    return countries

def read_users_csv(path):
    users = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            user = Users(
                id=int(row['id']),
                name=row['name'],
                email=row['email'],
                country_code=row['country_code'],
                created_at=datetime.strptime(row['created_at'], "%Y-%m-%d")
            )
            users.append(user)
            print(f"Cargando usuario: id={user.id}, nombre={user.name}, email={user.email}, pais={user.country_code}")
    print(f"Total usuarios leídos: {len(users)}")
    return users

def read_products_csv(path):
    products = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(
                Products(
                    id=int(row['id']),
                    name=row['name'],
                    price=float(row['price']),
                    category_id=int(row['category_id'])
                )
            )
    return products

def read_product_details_csv(path):
    details = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            details.append(
                ProductDetails(
                    product_id=int(row['product_id']),
                    stock=int(row['stock']),
                    rating=float(row['rating']),
                    weight=float(row['weight'])
                )
            )
    return details

def read_orders_csv(path):
    orders = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            orders.append(
                Orders(
                    id=int(row['id']),
                    user_id=int(row['user_id']),
                    order_date=datetime.strptime(row['order_date'], "%Y-%m-%d"),
                    total_amount=float(row['total_amount'])
                )
            )
    return orders

def read_order_items_csv(path):
    items = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(
                OrderItems(
                    id=int(row['id']),
                    order_id=int(row['order_id']),
                    product_id=int(row['product_id']),
                    quantity=int(row['quantity']),
                    unit_price=float(row['unit_price'])
                )
            )
    return items

def read_shipping_regions_csv(path):
    regions = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            regions.append(
                ShippingRegion(
                    country_code=row['country_code'],
                    region=row['region'],
                    shipping_zone=row['shipping_zone'],
                    estimated_days=int(row['estimated_days'])
                )
            )
    return regions