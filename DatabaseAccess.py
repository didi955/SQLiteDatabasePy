import sqlite3


class DatabaseAccess:

    def __init__(self, file):
        self.connection = None
        self.file = file

    def setupConnection(self):
        self.connection = sqlite3.connect(self.file)

    def getConnection(self) -> sqlite3.Connection:
        return self.connection

    def getFileDB(self):
        return self.file

    def init(self):
        self.setupConnection()

    def stop(self):
        self.connection.close()
