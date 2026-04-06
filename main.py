from db_utils import connect_db
from insertions import insert_category
from helpers import read_categories_csv
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

conn = connect_db()

# Fetch variables
DATABASE_URL = os.getenv("DATABASE_URL")



categories = read_categories_csv("data/categories.csv")
try:
    for category in categories:
        insert_category(conn, category)
    print("Categorias insertadas correctamente")
except Exception as e:
    print(f"Error al insertar: {e}")