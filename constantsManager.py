import constants
from ui import UI
from constantDao import  ConstantDao
from cryptographyUtils import CryptographyUtils


class ConstantsManager:
    __constant_dao = ConstantDao()
    __ui = UI()
    __crypto = None


    def __init__(self, passphrase: str):
      self.__crypto = CryptographyUtils(passphrase)
      self.init_constantes()
    

    def init_constantes(self):
      """
      Verify and initialize database and constants if necessary
      """
      print("\n-- Chekc if table 'constants' exist")
      # Boolean table
      is_table_exist = False
      # Boolean keys
      is_keys_view_id_exist = False
      is_keys_telegram_group_id_exist = False
      is_keys_telegram_bot_token_exist = False
      # Boolean values
      is_value_view_id_has_value = False
      is_value_telegram_group_id_has_value = False
      is_value_telegram_bot_token_has_value = False
      # Check if 'constants' table exist
      is_table_exist = self.__constant_dao.verify_if_table_exist("constants")

      if not is_table_exist:
        self.__constant_dao.create_constants_table()

      self.__ui.print_message("\n-- Check if key column is not empty in 'constants'")
      is_keys_view_id_exist = self.__constant_dao.verify_if_key_column_have_value(constants.STR_VIEW_ID)
      is_keys_telegram_group_id_exist = self.__constant_dao.verify_if_key_column_have_value(constants.STR_TELEGRAM_GROUP_ID)
      is_keys_telegram_bot_token_exist = self.__constant_dao.verify_if_key_column_have_value(constants.STR_TELEGRAM_BOT_TOKEN)
      
      if is_keys_view_id_exist & is_keys_telegram_group_id_exist & is_keys_telegram_bot_token_exist:
        self.__ui.print_message("\n-- Check if value column is not empty in 'constants'")
        is_value_view_id_has_value = self.__constant_dao.verify_if_value_column_have_value(constants.STR_VIEW_ID)
        is_value_telegram_group_id_has_value = self.__constant_dao.verify_if_value_column_have_value(constants.STR_TELEGRAM_GROUP_ID)
        is_value_telegram_bot_token_has_value = self.__constant_dao.verify_if_value_column_have_value(constants.STR_TELEGRAM_BOT_TOKEN)
      else:
        self.__ui.print_message("\n-- Insert keys in 'constants' table")
        self.__constant_dao.insert_constants_key(constants.STR_VIEW_ID)
        self.__constant_dao.insert_constants_key(constants.STR_TELEGRAM_GROUP_ID)
        self.__constant_dao.insert_constants_key(constants.STR_TELEGRAM_BOT_TOKEN)

      if is_value_view_id_has_value & is_value_telegram_group_id_has_value & is_value_telegram_bot_token_has_value:
        self.__ui.print_message("Database is ready!")
      else:
        UI_PRINT = "Enter the value for {} key: "
        self.__ui.print_message("\n-- Insert values in 'constants' table")

        view_id = self.__ui.get_user_entry(UI_PRINT.format(constants.STR_VIEW_ID))
        self.__constant_dao.update_constant(constants.STR_VIEW_ID, self.__crypto.encrypt(view_id))
        self.__ui.print_message("")

        telegram_bot_token = self.__ui.get_user_entry(UI_PRINT.format(constants.STR_TELEGRAM_BOT_TOKEN))
        self.__constant_dao.update_constant(constants.STR_TELEGRAM_BOT_TOKEN, self.__crypto.encrypt(telegram_bot_token))
        self.__ui.print_message("")

        telegram_group_id = self.__ui.get_user_entry(UI_PRINT.format(constants.STR_TELEGRAM_GROUP_ID))
        self.__constant_dao.update_constant(constants.STR_TELEGRAM_GROUP_ID, self.__crypto.encrypt(telegram_group_id))
        self.__ui.print_message("")


    def getConstantValue(self, constantKey):
      return self.__crypto.decrypt(self.__constant_dao.get_constant(constantKey))