import telebot

bot= telebot.TeleBot('1503126735:AAFV3VXs-j2qwz1GCkwb3OcASlGKJzoT16M')

@bot.message_handler(comands=["start"])
def start(message):

    bot.send_game(chat_id=message.chat.id,game_short_name='testgame')

if  __name__ == "__main__":
    bot.polling()
