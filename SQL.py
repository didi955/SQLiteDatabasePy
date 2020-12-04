import sqlite3


def update(connection: sqlite3.Connection, qry: str, *args):
    cursor = connection.cursor()
    if len(args) == 0:
        cursor.execute(qry)
    else:
        for arg in args:
            cursor.execute(qry, arg)
    connection.commit()
    cursor.close()


def queryAll(connection: sqlite3.Connection, qry: str, *args) -> list:
    cursor = connection.cursor()
    if len(args) == 0:
        cursor.execute(qry)
    else:
        for arg in args:
            cursor.execute(qry, arg)
    rs = cursor.fetchall()
    return rs


def queryOne(connection: sqlite3.Connection, qry: str, *args) -> list:
    cursor = connection.cursor()
    if len(args) == 0:
        cursor.execute(qry)
    else:
        for arg in args:
            cursor.execute(qry, arg)
    rs = cursor.fetchone()
    return rs
