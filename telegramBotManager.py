import telegram
import os
import constants

class TelegramBotManager:
    bot = telegram.Bot(token=constants.TELEGRAM_BOT_TOKEN)

    def send_message_to_group(self, id_group, message):
        """
        Method for send message with bot on specify group
        """
        # Send message to group
        self.bot.send_message(chat_id=id_group, text=message)