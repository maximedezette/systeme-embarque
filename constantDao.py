import os
import sqlite3
import constants

class ConstantDao:
    __DB_FILE = "embeded_conception.db"
    __EXCEPTION_TITLE = "-- Exception: "
    __sqlite_connection = sqlite3.connect(__DB_FILE)
    __cursor = None

    def __init__(self):
        try:
            self.__check_init_cursor()
        except Exception as exception:
            print(str(exception))


    def get_constant(self, key):
        """
        Get constant value by his key
        """
        try:
            print("-- Get key: " + str(key))
            self.__check_init_cursor()
            self.__cursor.execute("SELECT key, value FROM constants WHERE key = ?;", (key,))
            results = self.__cursor.fetchall()
            if (len(results) > 0) & (results[0][0] == key):
                return results[0][1]
        except Exception as exception:
            print(self.__EXCEPTION_TITLE + str(exception))
            return None


    def update_constant(self, key, value):
        """
        Update constant into database
        """
        try:
            print("Update constant " + str(key) + " into database")
            self.__check_init_cursor()
            self.__cursor.execute("UPDATE constants SET value=? WHERE key = ?;", (value, key))
            self.__sqlite_connection.commit()
        except Exception as exception:
            print(self.__EXCEPTION_TITLE + str(exception))


    def create_constants_table(self):
        """
        Create table and add constants keys (VIEW_ID, TELEGRAM_GROUP_ID, TELEGRAM_BOT_TOKEN)
        """
        try:
            self.__check_init_cursor()
            self.__cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='constants';")
            results = self.__cursor.fetchall()
            if results[0][0] == 0:
                print("-- Create table 'constants'")
                self.__cursor.execute("CREATE TABLE constants(key TEXT NOT NULL UNIQUE, value TEXT NOT NULL);")
            self.__sqlite_connection.commit()
        except Exception as exception:
            print(self.__EXCEPTION_TITLE + str(exception))


    def insert_constants_key(self, key):
        """
        """
        self.__check_init_cursor()
        SELECT_QUERY = "SELECT key FROM constants WHERE key = ?;"
        INSERT_QUERY = "INSERT INTO constants(key, value) VALUES (?, '');"

        self.__cursor.execute(SELECT_QUERY, (key,))
        results = self.__cursor.fetchall()
        print(results)
        if len(results) == 0:
            print("-- Insert key " + str(constants.STR_VIEW_ID))
            self.__cursor.execute(INSERT_QUERY, (key,))

        self.__sqlite_connection.commit()


    def reset_database(self):
        """
        Reset database, delete database file
        """
        try:
            print("-- Reset database")
            if self.__sqlite_connection != None:
                print("-- Close SQLite connection")
                self.__sqlite_connection.close()
                
            print("-- Drop database file")
            os.remove(self.__DB_FILE)
        except Exception as exception:
            print(self.__EXCEPTION_TITLE + str(exception))


    def verify_if_table_exist(self, table_name):
        """
        Verify if table exist
        """
        self.__check_init_cursor()
        is_ok = True

        self.__cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))
        results = self.__cursor.fetchall()

        if results[0][0] == 0:
            print("Missing table 'constants'")
            is_ok = False
        else:
            print("'constants' table exist")
        
        return is_ok


    def verify_if_key_column_have_value(self, key):
        """
        Verifiy if key column have value
        """
        self.__check_init_cursor()
        is_ok = True
        SELECT_QUERY = "SELECT key FROM constants WHERE key = ?;"

        self.__cursor.execute(SELECT_QUERY, (key,))
        results = self.__cursor.fetchall()
        if len(results) == 0:
            print("Missing key value: " + str(key))
            is_ok = False

        return is_ok


    def verify_if_value_column_have_value(self, key):
        """
        Verify if value column have value
        """
        self.__check_init_cursor()
        is_ok = True
        SELECT_QUERY = "SELECT value FROM constants WHERE key = ?;"

        self.__cursor.execute(SELECT_QUERY, (key,))
        results = self.__cursor.fetchall()
        
        if len(results[0][0]) <= 9:
            print("Missing value for key: " + str(key))
            is_ok = False

        return is_ok


    def __check_init_cursor(self):
        if self.__cursor == None:
            self.__cursor = self.__sqlite_connection.cursor()