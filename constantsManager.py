import sqlite3
import constants
from sqlite3 import Error

class ConstantsManager:

    def init_constantes(self):
      try:
        con = sqlite3.connect('monitorwebsite.db')
      except:
        print("Impossible de se connecter a la BDD")

      cursor_obj = con.cursor()
    
      cursor_obj.execute('SELECT * FROM constants')
    
      rows = cursor_obj.fetchall()  
      for row in rows:
        print(row)
        if row[0] == constants.STR_VIEW_ID:
          constants.VIEW_ID = row[1]
        elif row[0] == constants.STR_TELEGRAM_GROUP_ID:
          constants.TELEGRAM_GROUP_ID = row[1]
        elif row[0] == constants.STR_TELEGRAM_BOT_TOKEN:
          constants.TELEGRAM_BOT_TOKEN = row[1]