import sqlite3
from contextlib import contextmanager

@contextmanager
def database_connection_manager(url):

    conn = None

    try:
        print(f"Connecting to DB {url}")
        conn = sqlite3.connect(url)

        yield conn

    finally:

        if conn:
            print(f"Closing connection to DB {url}")
            conn.close()