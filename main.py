import telebot
# импорт auth_data.py переменной token
from auth_data import token


def get_telebot():
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, message.text)

    @bot.message_handler(content_types=['text'])
    def send_name(message):
        if message.text == "secret":
            bot.reply_to(
                message,
                f"How must DIE!!!!!")
        else:
            bot.reply_to(
                message,
                f"Welcome {message.from_user.first_name} what does this '{message.text}' mean ?")

    bot.infinity_polling()


if __name__ == '__main__':
    get_telebot()
