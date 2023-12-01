import psycopg2


def get_conn():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database='postgres',
        user='postgres',
        password='postgres'
    )

    return conn
