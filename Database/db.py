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
            self.connection.commit()

    def insert_users_tg(self, Telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql.insert_telegram_users,
            (None, Telegram_id, username, first_name, last_name)
        )

        self.connection.commit()