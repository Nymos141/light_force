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

CREATE_BAN_USER_TABLE = """
CREATE TABLE IF NOT EXISTS ban_users 
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
BAN_COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""

insert_telegram_ban_users = """
insert or ignore into ban_users values (?,?,?)
"""

select_telegram_ban_users = """
select * from ban_users where telegram_id = ?
"""

update_telegram_ban_users = """
update ban_users set ban_count = ban_count +1 where telegram_id = ?
"""