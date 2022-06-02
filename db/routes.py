import psycopg2

from config import config

params = config()


class Database:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()


test = Database()
