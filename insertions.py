

def insert_category(conn, category):
    print(category.id)
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO categories (id, slug, name)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
            """,
            (category.id, category.slug, category.name)
        )
        conn.commit()