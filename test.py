import os

from telegramBotManager import TelegramBotManager
tbm = TelegramBotManager()

# Telegram group ID
TELEGRAM_GROUP_ID = os.environ.get('TelegramAperoTechGroupId')

# Call method for send message
tbm.send_message_to_group(TELEGRAM_GROUP_ID, 'Test! :D')