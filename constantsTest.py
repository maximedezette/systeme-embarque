import unittest
from constantsManager import ConstantsManager
import constants

class ConstantsTest(unittest.TestCase):


    def testConstantsShouldBeEmpty(self):
        self.assertEqual('', constants.VIEW_ID)
        self.assertEqual('', constants.TELEGRAM_GROUP_ID)
        self.assertEqual('', constants.TELEGRAM_BOT_TOKEN)

    def testConstantsShouldBeFilledAfterInit(self):

        constantManager = ConstantsManager()
        constantManager.initConstantes()
        self.assertGreater(len(constants.VIEW_ID),0)
        self.assertGreater(len(constants.TELEGRAM_GROUP_ID),0)
        self.assertGreater(len(constants.TELEGRAM_BOT_TOKEN),0)
  

if __name__ == '__main__':
    unittest.main()