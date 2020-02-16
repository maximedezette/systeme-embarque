import os
import sqlite3
import constants

class ConstantDao:
    DB_FILE = "embeded_conception.db"
    EXCEPTION_TITLE = "-- Exception: "
    sqlite_connection = sqlite3.connect(DB_FILE)
    cursor = None

    def __init__(self):
        try:
            self.cursor = self.sqlite_connection.cursor()
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
            if len(results) > 0 & results[0][0] == key:
                return results[0][1]
        except Exception as exception:
            print(self.EXCEPTION_TITLE + str(exception))
            return None


    def update_constant(self, key, value):
        """
        Update constant into database
        """
        try:
            print("-- Update constant " + str(key) + " into database")
            self.cursor.execute("INSERT INTO constants(value) VALUES (?) WHERE key = ?", (value, key))
            self.sqlite_connection.commit()
        except Exception as exception:
            print(self.EXCEPTION_TITLE + str(exception))


    def initialize_database(self):
        """
        Create table and add constants keys (VIEW_ID, TELEGRAM_GROUP_ID, TELEGRAM_BOT_TOKEN)
        """
        try:
            SELECT_QUERY = "SELECT key FROM constants WHERE key = ?;"
            INSERT_QUERY = "INSERT INTO constants(key, value) VALUES (?, '');"

            print("-- Database initialization")
            self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='constants';")
            results = self.cursor.fetchall()
            if len(results) == 0:
                print("-- Create table constants")
                self.cursor.execute("CREATE TABLE constants(key TEXT NOT NULL UNIQUE, value TEXT NOT NULL);")

            self.cursor.execute(SELECT_QUERY, (constants.STR_VIEW_ID,))
            results = self.cursor.fetchall()
            if len(results) == 0:
                print("-- Insert key VIEW_ID")
                self.cursor.execute(INSERT_QUERY, (constants.STR_VIEW_ID,))

            self.cursor.execute(SELECT_QUERY, (constants.STR_TELEGRAM_GROUP_ID,))
            results = self.cursor.fetchall()
            if len(results) == 0:
                print("-- Insert key TELEGRAM_GROUP_ID")
                self.cursor.execute(INSERT_QUERY, (constants.STR_TELEGRAM_GROUP_ID,))

            self.cursor.execute(SELECT_QUERY, (constants.STR_TELEGRAM_BOT_TOKEN,))
            results = self.cursor.fetchall()
            if len(results) == 0:
                print("-- Insert key TELEGRAM_BOT_TOKEN")
                self.cursor.execute(INSERT_QUERY, (constants.STR_TELEGRAM_BOT_TOKEN,))

            self.sqlite_connection.commit()
        except Exception as exception:
            print(self.EXCEPTION_TITLE + str(exception))


    def reset_database(self):
        """
        Reset database, delete database file
        """
        try:
            print("-- Reset database")
            if self.sqlite_connection != None:
                print("-- Close SQLite connection")
                self.sqlite_connection.close()
                
            print("-- Drop database file")
            os.remove(self.DB_FILE)
        except Exception as exception:
            print(self.EXCEPTION_TITLE + str(exception))


    def database_verification(self):
        """
        Verify if database existe and constants are not empty
        """
        SELECT_QUERY = "SELECT key FROM constants WHERE key = ?;"
        is_ok = os.path.exists(self.DB_FILE)

        self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='constants';")
        results = self.cursor.fetchall()
        if len(results) == 0:
            is_ok = False
        
        self.cursor.execute(SELECT_QUERY, (constants.STR_VIEW_ID,))
        results = self.cursor.fetchall()
        if len(results) == 0:
            is_ok = False
        
        self.cursor.execute(SELECT_QUERY, (constants.STR_TELEGRAM_GROUP_ID,))
        results = self.cursor.fetchall()
        if len(results) == 0:
            is_ok = False
        
        self.cursor.execute(SELECT_QUERY, (constants.STR_TELEGRAM_BOT_TOKEN,))
        results = self.cursor.fetchall()
        if len(results) == 0:
            is_ok = False
        
        if is_ok:
            # Check VIEW_ID constant
            view_id = self.get_constant(constants.STR_VIEW_ID)
            # Check TELEGRAM_GROUP_ID constant
            telegram_group_id = self.get_constant(constants.STR_TELEGRAM_GROUP_ID)
            # Check TELEGRAM_BOT_TOKEN constant
            telegram_bot_token = self.get_constant(constants.STR_TELEGRAM_BOT_TOKEN)
            
            if (view_id == None or view_id == '' or view_id == ' '):
                is_ok = False

            if (telegram_group_id == None or telegram_group_id == '' or telegram_group_id == ' '):
                is_ok = False
                
            if (telegram_bot_token == None or telegram_bot_token == '' or telegram_bot_token == ' '):
                is_ok = False

        return is_ok