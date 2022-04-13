@bot.message_handler()
def user_text(message):
    if message.text == "Hello" or "Hi" or "hello" or "hi":
        bot.send_message(message.chat.id, "Hey!")
    elif message.text == "thanks" or "thanks!" or "Thanks" or "Thanks!":
        bot.send_message(message.chat.id, "You are welcome!")
    else:
        bot.send_message(message.chat.id, "Sorry, I dont get it.")

@bot.message_handler(commands=['help'])
def button(message):
    markup = types.ReplyKeyboardMarkup()
    help = types.KeyboardButton('Help')
    markup.add(help)
    bot.send_message(message.chat.id, "Push the button", reply_markup=markup)
