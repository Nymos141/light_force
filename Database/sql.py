sql_create_table = """
CREATE TABLE IF NOT EXISTS tg_users (
    id INTEGER PRIMARY KEY,
    Telegram_id INTEGER,
    user_name VARCHAR(50), 
    first_name VARCHAR(50), 
    last_name VARCHAR(50),
    reference_link TEXT,
    balance INTEGER,
    UNIQUE (Telegram_id)
)
"""

alter_user_table = """
ALTER TABLE tg_users ADD COLUMN reference_link TEXT;
"""

alter_userbalance_table = """
ALTER TABLE tg_users ADD COLUMN balance INTEGER;
"""


double_select_referral = """
SELECT
    coalesce(tg_users.balance, 0) AS balance,
    COUNT(referral.id) AS total_referrals
FROM 
    tg_users
LEFT JOIN 
    referral ON tg_users.telegram_id = referral.telegram_user_link_id
WHERE 
    tg_users.telegram_id = ?            
"""

insert_telegram_users = """
INSERT OR IGNORE INTO tg_users VALUES (?,?,?,?,?,?,?)
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
create_telegram_users_profile_table = """
create table if not exists telegram_users_profile (
id integer primary key, 
telegram_id integer,
nickname varchar(50),
biography text,
age integer,
zodiac varchar(50),
blood_type varchar(50),
favorite_car varchar(100),
photo text,
unique (telegram_id)
)
"""


CREATE_LIKE_TABLE_PROFILE = """
CREATE TABLE IF NOT EXISTS like_profile 
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
LIKE_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, LIKE_TELEGRAM_ID)
)
"""

create_telegram_user_link_table = """
create table if not exists telegram_user_link(
id integer primary key,
telegram_id integer,
referral_telegram_id,
unique (telegram_id, referral_telegram_id)
)
"""
CREATE_REFERENCE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS reference_users (
    id INTEGER PRIMARY KEY,
    referred_telegram_id INTEGER,
    referred_first_name VARCHAR(50),
    referred_username VARCHAR(50),
    UNIQUE (referred_telegram_id)
)
"""

INSERT_REFERENCE_USERS = """
INSERT INTO reference_users VALUES (?, ?, ?)
"""

select_refference_users = """
SELECT * FROM reference_users WHERE referred_telegram_id = ?
"""

CREATE_DISLIKE_TABLE_PROFILE = """
CREATE TABLE IF NOT EXISTS dislike_profile 
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
DISLIKE_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, DISLIKE_TELEGRAM_ID)
)
"""

INSERT_like_profile = """
INSERT INTO like_profile values (?,?,?)
"""

INSERT_dislike_profile = """
INSERT INTO dislike_profile values (?,?,?)
"""

FILTER_LEFT_JOIN_PROFILE = """
SELECT * FROM telegram_users_profile
LEFT JOIN like_profile ON telegram_users_profile.TELEGRAM_ID = like_profile.OWNER_TELEGRAM_ID
    AND like_profile.LIKE_TELEGRAM_ID = ?
LEFT JOIN dislike_profile ON telegram_users_profile.TELEGRAM_ID = dislike_profile.OWNER_TELEGRAM_ID
    AND dislike_profile.DISLIKE_TELEGRAM_ID = ?
WHERE like_profile.ID IS NULL
    AND dislike_profile.ID IS NULL
    AND telegram_users_profile.TELEGRAM_ID != ?
"""


insert_telegram_profile_user = """
insert or ignore into telegram_users_profile values (?,?,?,?,?,?,?,?,?)
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

select_profile_telegram_user = """
select * from telegram_users_profile where telegram_id = ?
"""

select_all_profile = """
select * from telegram_users_profile
"""

select_tg_users = """
select * from tg_users where Telegram_ID = ?
"""

update_tg_users = """
update tg_users set reference_link = ? where TELEGRAM_ID = ?
"""

create_news_link_table = """
create table if not exists news_link
(
id integer primary key,
telegram_id integer,
link text
)
"""

insert_news = """
INSERT INTO news_link VALUES (?, ?, ?)
"""

