import sqlite3


def update(connection: sqlite3.Connection, qry: str):
    cursor = connection.cursor()
    cursor.execute(qry)
    connection.commit()
    cursor.close()


def query(connection: sqlite3.Connection, qry: str) -> list:
    cursor = connection.cursor()
    cursor.execute(qry)
    rs = cursor.fetchall()
    cursor.close()
    return rs
