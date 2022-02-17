import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["start"])
def start_message(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()