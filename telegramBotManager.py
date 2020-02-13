import telegram
import os
import constants

class TelegramBotManager:

    # Initialize Telegram bot
    def __init__(self):
        try:
            self = telegram.Bot(token=constants.TELEGRAM_BOT_TOKEN)
        except:
            print("Le bot n'a pas pu être initialisé")
            
    # Method for send message with bot on specify group
    def send_message_to_group(self, id_group, message):
        # Send message to group
        self.bot.send_message(chat_id=id_group, text=message)