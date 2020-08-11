import datetime
import random
from telegram.ext import BaseFilter

from src.utils import *

CLTL_TOKEN = read_token()
intents = read_intents()
greetings = ('hello', 'hi', 'greetings', 'sup')
toxic = ('stupid', 'moron')


# Tailor made filters
class FilterGreetings(BaseFilter):
    def filter(self, message):
        return message.text.lower() in greetings


class FilterToxic(BaseFilter):
    def filter(self, message):
        return message.text.lower() in toxic


class FilterIntents(BaseFilter):
    def filter(self, message):
        for i in intents['intents']:
            if message.text in i['patterns']:
                print("Type of intent is: {}".format(i["tag"]))
                return True

        return False


# Actual processes
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def greet(update, context):
    now = datetime.datetime.now()
    hour = now.hour

    last_chat_name = update.message.chat.first_name
    greeting = ''

    if 6 <= hour < 12:
        greeting = 'Good Morning  {}'.format(last_chat_name)
    elif 12 <= hour < 17:
        greeting = 'Good Afternoon {}'.format(last_chat_name)
    elif 17 <= hour < 23:
        greeting = 'Good Evening  {}'.format(last_chat_name)

    context.bot.send_message(chat_id=update.effective_chat.id, text=greeting)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def respond_intent(update, context):
    response = "I am in an intent"

    for i in intents['intents']:
        if update.message.text in i['patterns']:
            response = random.choice(i['responses'])
            break

    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
