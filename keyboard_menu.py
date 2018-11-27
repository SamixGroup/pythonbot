# -*- coding: utf-8 -*-
# Bu fayl botda har xil oddiy menyular yaratishda foydalaniladi
import telebot
import config
bot = telebot.TeleBot(config.token) # Bu yerga token yoziladi


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False) #ReplyKeyboardMarkup class obyekti yaratilishi
    user_markup.row('/start', '/stop') # Bu qatordagi ' ' belgi ichidagilarni o'zgartiring
    user_markup.row('Bot', 'Guruh', 'Kanal') # Bu qatordagi ' ' belgi ichidagilarni o'zgartiring
    user_markup.row('Security') # Bu qatordagi ' ' belgi ichidagilarni o'zgartiring
    bot.send_message(message.from_user.id, 'Botga xush kelibsiz', reply_markup=user_markup)

if __name__=='__main__':
  bot.polling(none_stop=True)
