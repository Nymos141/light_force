sql_create_user_table = """
CREATE TABLE IF NOT EXISTS tg_users (
    id INTEGER PRIMARY KEY,
    Telegram_id INTEGER,
    user_name VARCHAR(50), 
    first_name VARCHAR(50), 
    last_name VARCHAR(50),
    reference_link text,
    balance integer,
    UNIQUE (Telegram_id)
    
)
"""

