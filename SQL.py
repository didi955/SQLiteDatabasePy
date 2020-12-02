import sqlite3


def updatep(connection: sqlite3.Connection, qry: str, *args):
    cursor = connection.cursor()
    for arg in args:
        cursor.execute(qry, arg)
    connection.commit()
    cursor.close()


def update(connection: sqlite3.Connection, qry: str):
    cursor = connection.cursor()
    cursor.execute(qry)
    connection.commit()
    cursor.close()


def query(connection: sqlite3.Connection, qry: str) -> list:
    cursor = connection.cursor()
    cursor.execute(qry)
    rs = cursor.fetchall()
    return rs
