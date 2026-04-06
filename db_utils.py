import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def connect_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        print("Conexión exitosa")
        return conn
    except Exception as e:
        print("Error al conectar:", e)
        return None
    

def create_tables(conn):
    queries = [
        """
        CREATE TABLE IF NOT EXISTS categories (
            id INT PRIMARY KEY,
            slug TEXT,
            name TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS countries (
            code TEXT PRIMARY KEY,
            name TEXT,
            region TEXT,
            population BIGINT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS currency_rates (
            currency_code TEXT PRIMARY KEY,
            rate_to_usd FLOAT,
            updated_at TIMESTAMP
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT PRIMARY KEY,
            name TEXT,
            email TEXT,
            country_code TEXT REFERENCES countries(code),
            created_at TIMESTAMP
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS products (
            id INT PRIMARY KEY,
            name TEXT,
            price FLOAT,
            category_id INT REFERENCES categories(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS product_details (
            product_id INT PRIMARY KEY REFERENCES products(id),
            stock INT,
            rating FLOAT,
            weight FLOAT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS orders (
            id INT PRIMARY KEY,
            user_id INT REFERENCES users(id),
            order_date TIMESTAMP,
            total_amount FLOAT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS order_items (
            id INT PRIMARY KEY,
            order_id INT REFERENCES orders(id),
            product_id INT REFERENCES products(id),
            quantity INT,
            unit_price FLOAT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS shipping_regions (
            country_code TEXT REFERENCES countries(code),
            region TEXT,
            shipping_zone TEXT,
            estimated_days INT,
            PRIMARY KEY (country_code, region)
        );
        """
    ]

    with conn.cursor() as cur:
        for q in queries:
            cur.execute(q)
        conn.commit()
    print("Tablas creadas correctamente")
    
try:
    create_tables(connect_db())
    print("Tablas creadas exitosamente")
except Exception as e:
    print(F"Error de DB: {e}")