import csv
from models import Category

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