from .connect import get_connect

def insert_user(fullname, phone, gender, address, chat_id):
    try:
        with get_connect() as db:
            with db.cursor() as dbc:
                dbc.execute("""
                    INSERT INTO users (fullname, phone, address, chat_id, gender)
                    VALUES (%s, %s, %s, %s, %s)
                """, (fullname, phone, address, chat_id, gender))
                db.commit()
                return True
    except Exception as err:
        print(f"user save error: {err}")
        return None
