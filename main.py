import time
import constants

from ui import UI
from constantsManager import ConstantsManager



def main():
  ui = UI()

  ui.print_message("-- Passphrase for encryption database")
  cm = ConstantsManager(ui.get_user_entry("Enter passphrase: "))
  constants.VIEW_ID = cm.getConstantValue(constants.STR_VIEW_ID)
  constants.TELEGRAM_BOT_TOKEN = cm.getConstantValue(constants.STR_TELEGRAM_BOT_TOKEN)
  constants.TELEGRAM_GROUP_ID = cm.getConstantValue(constants.STR_TELEGRAM_GROUP_ID)

  from infoFactory import InfoFactory
  from screenManager import ScreenManager
  from telegramBotManager import TelegramBotManager
  from info import Info

  screen_manager = ScreenManager()

  info_factory = InfoFactory()
  id_info_max = info_factory.get_number_of_info()
  id_info = 2
  
  screen_manager.lcd_init() 

  while True:
    #On repart de 0 si on a affiché la dernière info
    #sinon on passe à la suivante
    if id_info == id_info_max:
     id_info = 1
    else:
      id_info = id_info + 1

    info = Info()
    #On récupère l'info à afficher
    info = info_factory.generate_info(id_info)

    #On affiche l'info
    screen_manager.print_first_line(info.get_first_line())
    screen_manager.print_second_line(info.get_second_line())


    if(info.get_level() =="ERROR"):
      screen_manager.light_on_alert_led()
      try:
        tbm = TelegramBotManager()
        tbm.send_message_to_group(constants.TELEGRAM_GROUP_ID,info.get_telegram_message())
      except:
        print ("Erreur lors de l'envoi de message par le Bot Telegram")
    else:
      if(bool(screen_manager.led_is_light())):
        screen_manager.light_off_alert_led()
        try:
          tbm = TelegramBotManager()
          tbm.send_message_to_group(constants.TELEGRAM_GROUP_ID,info.get_telegram_message())
        except:
          print ("Erreur lors de l'envoi de message par le Bot Telegram")
      
          
  
    time.sleep(10)

    #On efface le contenu de l'écran
    screen_manager.lcd_init()


if __name__ == '__main__':
  main()