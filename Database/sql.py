sql_create_table = """
CREATE TABLE IF NOT EXISTS tg_users (
    id INTEGER PRIMARY KEY,
    Telegram_id INTEGER,
    user_name VARCHAR(50), 
    first_name VARCHAR(50), 
    last_name VARCHAR(50), 
    UNIQUE (Telegram_id)
)
"""

insert_telegram_users = """
insert or ignore into tg_users values (?,?,?,?,?)
"""