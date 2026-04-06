import psycopg2
from psycopg2.extras import execute_values


def _bulk_insert(conn, query, rows, page_size=500):
    if not rows:
        return

    try:
        with conn.cursor() as cur:
            execute_values(cur, query, rows, page_size=page_size)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise


def insert_categories(conn, categories):
    rows = [
        (category.id, category.slug, category.name)
        for category in categories
    ]
    _bulk_insert(
        conn,
        "INSERT INTO categories (id, slug, name) VALUES %s ON CONFLICT (id) DO NOTHING",
        rows
    )


def insert_countries(conn, countries):
    rows = [
        (
            country.code,
            country.name,
            country.region,
            getattr(country, 'population', 0) or 0
        )
        for country in countries
    ]
    _bulk_insert(
        conn,
        "INSERT INTO countries (code, name, region, population) VALUES %s ON CONFLICT (code) DO NOTHING",
        rows
    )


def insert_users(conn, users):
    rows = [
        (user.id, user.name, user.email, user.country_code, user.created_at)
        for user in users
    ]
    _bulk_insert(
        conn,
        "INSERT INTO users (id, name, email, country_code, created_at) VALUES %s ON CONFLICT (id) DO NOTHING",
        rows
    )


def insert_products(conn, products):
    rows = [
        (product.id, product.name, product.price, product.category_id)
        for product in products
    ]
    _bulk_insert(
        conn,
        "INSERT INTO products (id, name, price, category_id) VALUES %s ON CONFLICT (id) DO NOTHING",
        rows
    )


def insert_product_details(conn, details):
    rows = [
        (detail.product_id, detail.stock, detail.rating, detail.weight)
        for detail in details
    ]
    _bulk_insert(
        conn,
        "INSERT INTO product_details (product_id, stock, rating, weight) VALUES %s ON CONFLICT (product_id) DO NOTHING",
        rows
    )


def insert_orders(conn, orders):
    rows = [
        (order.id, order.user_id, order.order_date, order.total_amount)
        for order in orders
    ]
    _bulk_insert(
        conn,
        "INSERT INTO orders (id, user_id, order_date, total_amount) VALUES %s ON CONFLICT (id) DO NOTHING",
        rows
    )


def insert_order_items(conn, items):
    rows = [
        (item.id, item.order_id, item.product_id, item.quantity, item.unit_price)
        for item in items
    ]
    _bulk_insert(
        conn,
        "INSERT INTO order_items (id, order_id, product_id, quantity, unit_price) VALUES %s ON CONFLICT (id) DO NOTHING",
        rows
    )


def insert_shipping_regions(conn, regions):
    rows = [
        (region.country_code, region.region, region.shipping_zone, region.estimated_days)
        for region in regions
    ]
    _bulk_insert(
        conn,
        "INSERT INTO shipping_regions (country_code, region, shipping_zone, estimated_days) VALUES %s ON CONFLICT (country_code, region) DO NOTHING",
        rows
    )