import os
import telebot

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    args = message.text.split()
    if len(args) > 1:
        bot.send_message(message.chat.id, " Вы успешно зарегистрировались!")
    else:
        bot.send_message(message.chat.id, "Привет! Перейдите из приложения для регистрации.")

if __name__ == '__main__':
    print("Бот успешно запущен на Koyeb!")
    bot.infinity_polling()
