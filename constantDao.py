import os
import sqlite3

class ConstantDao:
    sqliteConnection = sqlite3.connect("embeded_conception.db")
    cursor = None

    def __init__(self):
        try:
            self.cursor = self.sqliteConnection.cursor()
            # self.initializeDatabase()
            self.getConstant("VIEW_ID")
        except Exception as exception:
            print(str(exception))


    def getConstant(self, key):
        """
        Get constant value by his key
        """
        try:
            print("-- Get key: " + str(key))
            self.cursor.execute("SELECT key,value FROM constants WHERE key = ?", (key,))
            results = self.cursor.fetchall()
            if len(results) > 0:
                if results[0][0] == key:
                    print(results[0][1])
                    return results[0][1]
        except Exception as exception:
            print("-- Exception: " + str(exception))


    def updateConstant(self, key, value):
        """
        Update constant into database
        """
        print("-- Update constant into database")


    def initializeDatabase(self):
        """
        Create table and add constants keys (VIEW_ID, TELEGRAM_GROUP_ID, TELEGRAM_BOT_TOKEN)
        """
        try:
            print("-- Database initialization")
            result = self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='constants';")
            if result.fetchone()[0] == 0:
                print("-- Create table constants")
                self.cursor.execute("CREATE TABLE constants(key TEXT NOT NULL UNIQUE, value TEXT NOT NULL);")

            results = self.cursor.execute("SELECT key FROM constants WHERE key = 'VIEW_ID';")
            if results.fetchone() == None:
                print("-- Insert key VIEW_ID")
                self.cursor.execute("INSERT INTO constants(key, value) VALUES ('VIEW_ID', '');")

            results = self.cursor.execute("SELECT key FROM constants WHERE key = 'TELEGRAM_GROUP_ID';")
            if results.fetchone() == None:
                print("-- Insert key TELEGRAM_GROUP_ID")
                self.cursor.execute("INSERT INTO constants(key, value) VALUES ('TELEGRAM_GROUP_ID', '');")

            results = self.cursor.execute("SELECT key FROM constants WHERE key = 'TELEGRAM_BOT_TOKEN';")
            if results.fetchone() == None:
                print("-- Insert key TELEGRAM_BOT_TOKEN")
                self.cursor.execute("INSERT INTO constants(key, value) VALUES ('TELEGRAM_BOT_TOKEN', '');")

            self.sqliteConnection.commit()
        except Exception as exception:
            print("-- Exception: " + str(exception))


    def resetDatabase(self):
        """
        Reset database, delete database file
        """
        try:
            print("-- Reset database")
            if self.sqliteConnection != None:
                print("-- Close SQLite connection")
                self.sqliteConnection.close()
                
            print("-- Drop database file")
            os.remove("embeded_conception.db")
        except Exception as exception:
            print("Exception: " + str(exception))


constantDao = ConstantDao()