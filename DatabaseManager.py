from enum import Enum
from DatabaseAccess import DatabaseAccess


class DatabaseManager(Enum):
    BDD1 = (open("database1.db", "w+"))

    def __init__(self):
        self.databaseAccess = DatabaseAccess(self.value)

    def getDatabaseAccess(self) -> DatabaseAccess:
        return self.databaseAccess

    @staticmethod
    def initAllDatabaseConnections():
        for key in DatabaseManager.__members__.values():
            key.databaseAccess.init()

    @staticmethod
    def closeAllDatabaseConnection():
        for key in DatabaseManager.__members__.values():
            key.databaseAccess.stop()
