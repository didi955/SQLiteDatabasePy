import sqlite3


class DatabaseAccess:

    def __init__(self, name, file):
        self.file = file
        self.name = name
        self.connection = None

    def getConnection(self) -> sqlite3.Connection:
        return self.connection

    def getFileDB(self):
        return self.file

    def init(self):
        self.connection = sqlite3.connect(self.name)

    def stop(self):
        self.connection.close()
