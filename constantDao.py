import sqlite3

class ConstantDao:
    sqliteConnection = sqlite3.connect("embeded_conception.db")
    cursor = None

    def __init__(self):
        try:
            self.cursor = self.sqliteConnection.cursor
            self.initializeDatabase()
        except Exception as exception:
            print(str(exception))

    def getAllConstants(self):
        print("-- Get all constants from database")

    def addConstant(self, key, value):
        print("-- Insert constant into database")

    def updateConstant(self, key, value):
        print("-- Update constant into database")

    def deleteConstant(self, key):
        print("-- Delete constant into database")

    def initializeDatabase(self):
        print("-- Database initialization")
        self.sqliteConnection.execute("CREATE TABLE constants(key TEXT, value TEXT)")
        # TODO: Insert keys with empty values
        self.sqliteConnection.commit()

constantDao = ConstantDao()