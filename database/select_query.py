from .connect import get_connect


def is_register_by_id(chat_id):
    try:
        with get_connect() as db:
            dbc = db.cursor()
            dbc.execute("SELECT * FROM users WHERE chat_id = ?", (chat_id,))
            return dbc.fetchone()
    except Exception as err:
        print(f"Register: {err}")
        return None


def get_filter_products(category_id, season, gender):
    try:
        with get_connect() as db:
            dbc = db.cursor()
            dbc.execute("""
                SELECT * FROM product 
                WHERE category_id = ? AND season = ? AND gender_type = ?
            """, (category_id, season, gender))
            return dbc.fetchall()
    except Exception as err:
        print(f"Filter Product: {err}")
        return None


def get_category_by_id(category_id):
    try:
        with get_connect() as db:
            dbc = db.cursor()
            dbc.execute("SELECT name FROM category WHERE id = ?", (category_id,))
            return dbc.fetchone()
    except Exception as err:
        print(f"Filter Category: {err}")
        return None


def get_category():
    try:
        with get_connect() as db:
            dbc = db.cursor()
            dbc.execute("SELECT id, name FROM category WHERE is_activate = 1")
            return dbc.fetchall()
    except Exception as err:
        print(f"Get Category: {err}")
        return None
