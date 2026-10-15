from psycopg2 import connect


class DBContextManager:
    def __init__(self, db_connect: dict):
        self.conn = None
        self.cursor = None
        self.db_connect = db_connect

    def __enter__(self):
        self.conn = connect(**self.db_connect)
        try:
            self.cursor = self.conn.cursor()
        except Exception:
            self.conn.close()
            raise
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                self.conn.rollback()
            else:
                self.conn.commit()
        finally:
            try:
                if self.cursor is not None:
                    self.cursor.close()
            finally:
                self.conn.close()
        return False
