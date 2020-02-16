from infoFactory import InfoFactory
from screenManager import ScreenManager
from constantsManager import ConstantsManager


import time
import constants


def main():

  constantManager = ConstantsManager()
  screenManager = ScreenManager()

  constantManager.initConstantes()

  infoFactory = InfoFactory()
  idInfoMax = infoFactory.getNumberOfInfo()
  idInfo = 2
  
  screenManager.lcd_init() 

  while True:

    #On repart de 0 si on a affiché la dernière info
    #sinon on passe à la suivante
    if idInfo == idInfoMax:
     idInfo = 1
    else:
      idInfo = idInfo + 1

    info = []
    #On récupère l'info à afficher
    info = infoFactory.generateInfo(idInfo)

    #On affiche l'info
    screenManager.print_first_line(info[0])

    if len(info)>1:
      screenManager.print_second_line(info[1])
  
    time.sleep(10)

    #On efface le contenu de l'écran
    screenManager.lcd_init()

if __name__ == '__main__':
  main()