from db_utils import connect_db, create_tables
from insertions import (
    insert_categories, insert_countries, insert_users, insert_products,
    insert_product_details, insert_orders, insert_order_items, insert_shipping_regions
)
from helpers import (
    read_categories_csv, read_countries_csv, read_users_csv, read_products_csv,
    read_product_details_csv, read_orders_csv, read_order_items_csv, read_shipping_regions_csv
)
from api import generar_csv_paises
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

print("=" * 60)
print("INICIANDO CARGA DE DATOS")
print("=" * 60)

# Paso 1: Generar CSV de países desde la API
print("\n📡 Paso 1: Generando CSV de países desde la API...")
print("-" * 60)
if generar_csv_paises():
    print("✓ CSV de países generado exitosamente\n")
else:
    print("✗ Error al generar CSV de países\n")

# Paso 2: Conectar a la base de datos
print("📊 Paso 2: Conectando a la base de datos...")
print("-" * 60)
conn = connect_db()
if not conn:
    print("✗ No se pudo conectar a la base de datos. Abortando.")
    exit(1)

# Paso 3: Crear tablas
print("\n📋 Paso 3: Creando tablas...")
print("-" * 60)
try:
    create_tables(conn)
except Exception as e:
    print(f"✗ Error al crear tablas: {e}")

# Paso 4: Cargar datos
print("\n📥 Paso 4: Cargando datos en la base de datos...")
print("-" * 60)

# Load and insert categories
print("\n▶ Insertando categorías...")
categories = read_categories_csv("data/categories.csv")
try:
    insert_categories(conn, categories)
    print(f"✓ {len(categories)} categorías insertadas correctamente")
except Exception as e:
    print(f"✗ Error al insertar categorías: {e}")
    conn.rollback()

# Load and insert countries
print("\n▶ Insertando países...")
countries = read_countries_csv("data/countries.csv")
try:
    insert_countries(conn, countries)
    print(f"✓ {len(countries)} países insertados correctamente")
except Exception as e:
    print(f"✗ Error al insertar países: {e}")
    conn.rollback()

# Load and insert users
print("\n▶ Insertando usuarios...")
users = read_users_csv("data/users.csv")
try:
    insert_users(conn, users)
    print(f"✓ {len(users)} usuarios insertados correctamente")
except Exception as e:
    print(f"✗ Error al insertar usuarios: {e}")
    conn.rollback()

# Load and insert products
print("\n▶ Insertando productos...")
products = read_products_csv("data/products.csv")
try:
    insert_products(conn, products)
    print(f"✓ {len(products)} productos insertados correctamente")
except Exception as e:
    print(f"✗ Error al insertar productos: {e}")
    conn.rollback()

# Load and insert product details
print("\n▶ Insertando detalles de productos...")
product_details = read_product_details_csv("data/product_details.csv")
try:
    insert_product_details(conn, product_details)
    print(f"✓ {len(product_details)} detalles de productos insertados correctamente")
except Exception as e:
    print(f"✗ Error al insertar detalles de productos: {e}")
    conn.rollback()

# Load and insert orders
print("\n▶ Insertando órdenes...")
orders = read_orders_csv("data/orders.csv")
try:
    insert_orders(conn, orders)
    print(f"✓ {len(orders)} órdenes insertadas correctamente")
except Exception as e:
    print(f"✗ Error al insertar órdenes: {e}")
    conn.rollback()

# Load and insert order items
print("\n▶ Insertando ítems de órdenes...")
order_items = read_order_items_csv("data/order_items.csv")
try:
    insert_order_items(conn, order_items)
    print(f"✓ {len(order_items)} ítems de órdenes insertados correctamente")
except Exception as e:
    print(f"✗ Error al insertar ítems de órdenes: {e}")
    conn.rollback()

# Load and insert shipping regions
print("\n▶ Insertando regiones de envío...")
shipping_regions = read_shipping_regions_csv("data/shipping_regions.csv")
try:
    insert_shipping_regions(conn, shipping_regions)
    print(f"✓ {len(shipping_regions)} regiones de envío insertadas correctamente")
except Exception as e:
    print(f"✗ Error al insertar regiones de envío: {e}")
    conn.rollback()

# Close connection
conn.close()
print("\n" + "=" * 60)
print("✓ CONEXIÓN CERRADA. CARGA DE DATOS COMPLETADA.")
print("=" * 60)