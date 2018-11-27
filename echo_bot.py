# -*- coding: utf-8 -*-
# Bu bot yozgan matningizni o'zingizga qaytarib junatadi
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Funksiya nomi hech qanday rol o'ynamaydi
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
