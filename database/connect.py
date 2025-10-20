from psycopg2 import connect
from environs import Env

env=Env()
env.read_env()


def get_connect():
    return connect(
        user=env.str("USER"),
        password=env.str("PASSWORD"),
        host=env.str("HOST"),
        port=env.str("PORT"),
        database=env.str("DATABASE")
    )

def create_table():
    sql="""
    -- Foydalanuvchilar jadvali
CREATE TABLE IF NOT EXISTS admin (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(200 ) NOT NULL,
    phone VARCHAR(50) UNIQUE NOT NULL,
    address TEXT NOT NULL,
    chat_id BIGINT UNIQUE NOT NULL,
    gender VARCHAR(50 ),
    is_admin BOOLEAN DEFAULT FALSE,
    is_block BOOLEAN DEFAULT FALSE
);

-- Kategoriyalar jadvali
CREATE TABLE IF NOT EXISTS category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Mahsulotlar jadvali
CREATE TABLE IF NOT EXISTS product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    image TEXT NOT NULL,
    price BIGINT NOT NULL,
    quantity INT DEFAULT 0,
    size VARCHAR(50),
    season VARCHAR(20),
    gender_type VARCHAR(20),
    brand VARCHAR(50),
    category_id INT REFERENCES category(id) ON DELETE CASCADE
);

-- Buyurtmalar jadvali
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    product_id INT REFERENCES product(id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    price BIGINT NOT NULL,
    status VARCHAR(50) DEFAULT 'new'
);

    """

    with get_connect() as db:
        with db.cursor() as dbc:
            dbc.execute(sql)
            db.commit()
create_table() 