import telegram
import os

class TelegramBotManager:

    TELEGRAM_BOT_TOKEN = os.environ.get('TelegramBotToken')
    # Initialize Telegram bot
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

    # Method for send message with bot on specify group
    def send_message_to_group(self, id_group, message):
        # Send message to group
        self.bot.send_message(chat_id=id_group, text=message)