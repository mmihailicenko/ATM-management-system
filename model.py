import sqlite3


class SQLite:
    def __init__(self, file='application.db'):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        print("Database connection closed")
        self.conn.close()


class NotFoundError(Exception):
    pass


def atms_list_to_json(item):
    return {
        'id': item[0],
        'name': item[1],
        'location': item[2],
        'blocked': bool(item[3])
    }


def fetch_atms():
    try:
        with SQLite('application.db') as cur:
            cur.execute('SELECT * FROM atms')

            return list(map(atms_list_to_json, cur.fetchall()))
    except sqlite3.OperationalError as e:
        print(e)
        return []


def fetch_atm(id: str):
    try:
        with SQLite('application.db') as cur:

            # execute the query and fetch the data
            cur.execute(f"SELECT * FROM atms where id=?", [id])
            result = cur.fetchone()

            # return the result or raise an error
            if result is None:
                raise NotFoundError(f'Unable to find blog with id {id}.')

            data = atms_list_to_json(result)
            return data
    except sqlite3.OperationalError:
        raise NotFoundError(f'Unable to find blog with id {id}.')
