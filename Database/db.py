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
            self.connection.execute(sql.create_telegram_users_profile_table)
            self.connection.execute(sql.CREATE_LIKE_TABLE_PROFILE)
            self.connection.execute(sql.create_telegram_user_link_table)
            self.connection.execute(sql.CREATE_DISLIKE_TABLE_PROFILE)
            self.connection.execute(sql.CREATE_REFERENCE_USERS_TABLE)

            try:
                self.connection.execute(sql.alter_user_table)
                self.connection.execute(sql.alter_userbalance_table)
            except sqlite3.OperationalError:
                pass
            self.connection.commit()

    def insert_users_tg(self, Telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql.insert_telegram_users,
            (None, Telegram_id, username, first_name, last_name, None, 0)
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

    def insert_telegram_profile(self, telegram_id, nickname, biography,
                                age, zodiac, blood_type, favorite_car, photo):
        self.cursor.execute(
            sql.insert_telegram_profile_user,
            (None, telegram_id, nickname, biography, age,
             zodiac, blood_type, favorite_car, photo)
        )
        self.connection.commit()

    def sql_select_profile(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'nickname': row[2],
            'biography': row[3],
            'age': row[4],
            'zodiac': row[5],
            'blood_type': row[6],
            'favorite_car': row[7],
            'photo': row[8]
        }
        return self.cursor.execute(
            sql.select_profile_telegram_user,
            (telegram_id,)
        ).fetchone()

    def insert_like(self, owner, like_telegram_id):
        self.cursor.execute(
            sql.INSERT_like_profile,
            (None, owner, like_telegram_id)
        )
        self.connection.commit()

    def insert_dislike(self, owner,  dislike_telegram_id):
        self.cursor.execute(
            sql.INSERT_like_profile,
            (None, owner, dislike_telegram_id)
        )
        self.connection.commit()

    def sql_select_all_profile(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'nickname': row[2],
            'biography': row[3],
            'age': row[4],
            'zodiac': row[5],
            'blood_type': row[6],
            'favorite_car': row[7],
            'photo': row[8]
        }
        return self.cursor.execute(
            sql.FILTER_LEFT_JOIN_PROFILE,
            (owner, owner,)
        ).fetchall()

    def sql_select_referral_menu(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            'balance': row[0],
            'total_referrals': row[1],
        }
        return self.cursor.execute(
            sql.double_select_referral,
            (owner,)
        ).fetchall()

    def select_tg_users(self, telegram_id):
        self.cursor.row_factory, = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'user_name': row[2],
            'first_name': row[3],
            'last_name': row[4],
            'balance': row[5],
            'total_referrals': row[6]
        }
        return self.cursor.execute(
            sql.select_tg_users,
            (telegram_id,)
        ).fetchone()

    def update_tg_users(self, reference_link, telegram_id):
        self.cursor.execute(
            sql.update_tg_users, (reference_link, telegram_id)
        )
        self.connection.commit()

    def insert_reference_users(self, referred_telegram_id, referred_first_name, referred_username):
        self.cursor.execute(
            sql.INSERT_REFERENCE_USERS,
            (referred_telegram_id, referred_first_name, referred_username)
        )
        self.connection.commit()

    def select_reference_users(self, owner_telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'referred_telegram_id': row[1],
            'referred_first_name': row[2],
            'referred_username': row[3]
        }
        return self.cursor.execute(
            sql.select_refference_users,
            (owner_telegram_id,)
        ).fetchall()



