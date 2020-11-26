from enum import Enum
from DatabaseAccess import DatabaseAccess


class DatabaseManager(Enum):
    BDD1 = "database1.db"

    def __init__(self, file):
        self.databaseAccess = DatabaseAccess(self.value, file)
        self.file = open("database1.db", "w+")

    def getDatabaseAccess(self) -> DatabaseAccess:
        return self.databaseAccess

    @staticmethod
    def initAllDatabaseConnection():
        for key in DatabaseManager.__members__.values():
            key.databaseAccess.init()

    @staticmethod
    def closeAllDatabaseConnection():
        for key in DatabaseManager.__members__.values():
            key.databaseAccess.stop()
