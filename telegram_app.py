import telebot
from config import TOKEN
from fsm import *

bot = telebot.TeleBot(TOKEN)

order = []

@bot.message_handler(content_types=['text'])
def telegram_bot(message):
    global trigger_counter, order
    if message.text == '/start' or trigger_counter == 4:
        trigger_counter = 0
        order = []
        machine.set_state('choice_of_pizza_size')
    order += [message.text]
    if trigger_counter != 2:
        bot.send_message(message.chat.id, messages[test.state])
    else:
        bot.send_message(message.chat.id, messages[test.state].format(order[1], order[2]))
    test.trigger(triggers[trigger_counter])
    trigger_counter += 1


bot.polling(none_stop=True)
