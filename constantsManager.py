import sqlite3
import constants
from sqlite3 import Error

class ConstantsManager:



    def initConstantes(self):

      try:
        con = sqlite3.connect('monitorwebsite.db')
      except:
        print("Impossible de se connecter a la BDD")

    
      cursorObj = con.cursor()
    
      cursorObj.execute('SELECT * FROM constants')
    
      rows = cursorObj.fetchall()  
      for row in rows:
        print(row)
        if row[0] == 'VIEW_ID':
          constants.VIEW_ID = row[1]
        elif row[0] == 'TELEGRAM_GROUP_ID':
          constants.TELEGRAM_GROUP_ID = row[1]
        elif row[0] == 'TELEGRAM_BOT_TOKEN':
          constants.TELEGRAM_BOT_TOKEN = row[1]
