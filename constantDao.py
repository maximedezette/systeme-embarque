import os
import sqlite3

class ConstantDao:
    sqliteConnection = sqlite3.connect("embeded_conception.db")
    cursor = None

    def __init__(self):
        try:
            self.cursor = self.sqliteConnection.cursor()
        except Exception as exception:
            print(str(exception))


    def get_constant(self, key):
        """
        Get constant value by his key
        """
        try:
            print("-- Get key: " + str(key))
            self.cursor.execute("SELECT key,value FROM constants WHERE key = ?", (key,))
            results = self.cursor.fetchall()
            if len(results) > 0:
                if results[0][0] == key:
                    return results[0][1]
        except Exception as exception:
            print("-- Exception: " + str(exception))
            return None


    def update_constant(self, key, value):
        """
        Update constant into database
        """
        try:
            print("-- Update constant " + str(key) + " into database")
            self.cursor.execute("INSERT INTO constants(value) VALUES (?) WHERE key = ?", (value, key))
            self.sqliteConnection.commit()
        except Exception as exception:
            print("-- Exception: " + str(exception))


    def initialize_database(self):
        """
        Create table and add constants keys (VIEW_ID, TELEGRAM_GROUP_ID, TELEGRAM_BOT_TOKEN)
        """
        try:
            print("-- Database initialization")
            self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='constants';")
            results = self.cursor.fetchall()
            if len(results) == 0:
                print("-- Create table constants")
                self.cursor.execute("CREATE TABLE constants(key TEXT NOT NULL UNIQUE, value TEXT NOT NULL);")

            self.cursor.execute("SELECT key FROM constants WHERE key = 'VIEW_ID';")
            results = self.cursor.fetchall()
            if len(results) == 0:
                print("-- Insert key VIEW_ID")
                self.cursor.execute("INSERT INTO constants(key, value) VALUES ('VIEW_ID', '');")

            self.cursor.execute("SELECT key FROM constants WHERE key = 'TELEGRAM_GROUP_ID';")
            results = self.cursor.fetchall()
            if len(results) == 0:
                print("-- Insert key TELEGRAM_GROUP_ID")
                self.cursor.execute("INSERT INTO constants(key, value) VALUES ('TELEGRAM_GROUP_ID', '');")

            self.cursor.execute("SELECT key FROM constants WHERE key = 'TELEGRAM_BOT_TOKEN';")
            results = self.cursor.fetchall()
            if len(results) == 0:
                print("-- Insert key TELEGRAM_BOT_TOKEN")
                self.cursor.execute("INSERT INTO constants(key, value) VALUES ('TELEGRAM_BOT_TOKEN', '');")

            self.sqliteConnection.commit()
        except Exception as exception:
            print("-- Exception: " + str(exception))


    def reset_database(self):
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


    def database_verification(self):
        """
        Verify if database existe and constants are not empty
        """
        isOk = os.path.exists("embeded_conception.db")

        self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='constants';")
        results = self.cursor.fetchall()
        if len(results) == 0:
            isOk = False
        
        self.cursor.execute("SELECT key FROM constants WHERE key = 'VIEW_ID';")
        results = self.cursor.fetchall()
        if len(results) == 0:
            isOk = False
        
        self.cursor.execute("SELECT key FROM constants WHERE key = 'TELEGRAM_GROUP_ID';")
        results = self.cursor.fetchall()
        if len(results) == 0:
            isOk = False
        
        self.cursor.execute("SELECT key FROM constants WHERE key = 'TELEGRAM_BOT_TOKEN';")
        results = self.cursor.fetchall()
        if len(results) == 0:
            isOk = False
        
        if isOk:
            # Check VIEW_ID constant
            viewId = self.get_constant("VIEW_ID")
            # Check TELEGRAM_GROUP_ID constant
            telegramGroupId = self.get_constant("TELEGRAM_GROUP_ID")
            # Check TELEGRAM_BOT_TOKEN constant
            telegramBotToken = self.get_constant("TELEGRAM_BOT_TOKEN")
            
            if (viewId == None or viewId == '' or viewId == ' '):
                isOk = False

            if (telegramGroupId == None or telegramGroupId == '' or telegramGroupId == ' '):
                isOk = False
                
            if (telegramBotToken == None or telegramBotToken == '' or telegramBotToken == ' '):
                isOk = False

        return isOk


constantDao = ConstantDao()