import telebot
from config import keys, TOKEN
from extensions import Converter, ConversionException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = (f"Welcome, {message.chat.username}! I'm GreatExchanger. I can help you to convert currencies.\n\
\nTo convert currencies please input as following: <Amount> <Currency> <Currency convert into>\n\
For example: 100 gbp rub\n\
\nTo get list of currencies: /values\n\
To get help - /help")
    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = (f"{message.chat.username} I can help you to convert currencies.\n\
\nTo convert currencies please input as following: <Amount> <Currency> <Currency convert into>\n\
For example: 100 gbp rub\n\
\nTo get list of currencies: /values\n")
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConversionException("Wrong parameters. Try again.\nFor example: 100 gbp rub")

        amount, quote, base = values
        total_base = Converter.convert(amount, quote, base)
    except ConversionException as e:
        bot.reply_to(message, f'Ohh my! Something wrong.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'I cannot execute your command\n{e}')
    else:
        text = f'Converting {amount} {quote} into {base}...\n\
Right now {amount} {quote} === {total_base * float(amount)} {base}.\nAnything else I can /help with?'
        bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)