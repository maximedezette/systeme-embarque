from info_factory import InfoFactory
from screen_manager import ScreenManager
from constants_manager import ConstantsManager

import time
import constants


def main():

  constants_manager = ConstantsManager()
  screen_manager = ScreenManager()

  constants_manager.init_constantes()

  info_factory = InfoFactory()
  id_info_max = info_factory.getNumberOfInfo()
  id_info = 2
  
  screen_manager.lcd_init() 

  while True:

    #On repart de 0 si on a affiché la dernière info
    #sinon on passe à la suivante
    if id_info == id_info_max:
     id_info = 1
    else:
      id_info = id_info + 1

    info = []
    #On récupère l'info à afficher
    info = info_factory.generateInfo(id_info)

    #On affiche l'info
    screen_manager.print_first_line(info[0])

    if len(info)>1:
      screen_manager.print_second_line(info[1])
  
    time.sleep(10)

    #On efface le contenu de l'écran
    screen_manager.lcd_init()

if __name__ == '__main__':
  main()