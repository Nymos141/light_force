import sqlite3
from Database import sql

class DATABASE:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create_table(self):
        if self.connection:
            print('joined')
            self.connection.execute(sql.sql_create_table)
            self.connection.execute(sql.CREATE_BAN_USER_TABLE)
            self.connection.commit()

    def insert_users_tg(self, Telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql.insert_telegram_users,
            (None, Telegram_id, username, first_name, last_name)
        )

        self.connection.commit()

    def insert_telegram_ban_users(self, telegram_id):
        self.cursor.execute(
            sql.insert_telegram_ban_users,
            (None, telegram_id, 1,)
        )
        self.connection.commit()

    def select_ban_user(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'count': row[2]
        }
        return self.cursor.execute(
            sql.select_telegram_ban_users,
            (telegram_id,)
        ).fetchone()

    def update(self, telegram_id):
        self.cursor.execute(
            sql.update_telegram_ban_users,
            (telegram_id,)
        )
        self.connection.commit()
