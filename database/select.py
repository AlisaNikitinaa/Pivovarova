from database.DBcm import DBContextManager
from flask import current_app


def select_list(_sql, user_list: list) -> list[tuple]:
    with DBContextManager(current_app.config['db_config']) as cursor:
        cursor.execute(_sql, user_list)
        return cursor.fetchall()
