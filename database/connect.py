from sqlite3 import connect
from environs import Env


def get_connect():
    return connect("optom_shop.sqlite3")



def create_table():
    tables = [
        """
        CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            address TEXT NOT NULL,
            chat_id INTEGER UNIQUE NOT NULL,
            gender TEXT NOT NULL,
            is_admin INTEGER DEFAULT 0,
            is_block INTEGER DEFAULT 0
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            is_active INTEGER DEFAULT 1
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            image TEXT NOT NULL,
            price INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            size TEXT,
            season TEXT,
            gender_type TEXT,
            brand TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category(id)
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            price INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            status TEXT DEFAULT 'new',
            FOREIGN KEY (chat_id) REFERENCES user (chat_id),
            FOREIGN KEY (product_id) REFERENCES product(id)
        );
        """
    ]


with get_connect() as db:
    cursor = db.cursor()
    for sql in tables:
        sql = sql.strip()
        if sql:
            cursor.execute(sql)
    db.commit()
    cursor.close()

create_table()
