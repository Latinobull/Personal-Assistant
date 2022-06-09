import psycopg2
from db.config import config


class Database:

    def __init__(self) -> None:
        params = config()
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def findUser(self):
        self.cur.execute('SELECT name FROM myuser')
        rows = self.cur.fetchall()
        return rows

    def createUser(self, name):
        self.cur.execute(
            "INSERT INTO myuser (name, location) VALUES (%s, %s)", (name, 'brooklyn'))
        self.conn.commit()
