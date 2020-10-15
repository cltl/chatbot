import datetime
import random
from telegram.ext import BaseFilter

from src.utils import *

CLTL_TOKEN = read_token()
intents = read_intents()
greetings = ('hello', 'hi', 'greetings', 'sup')


# Tailor made filters
class FilterGreetings(BaseFilter):
    def filter(self, message):
        return message.text.lower() in greetings


class FilterIntents(BaseFilter):
    def filter(self, message):
        intent = match_to_category(message, intents)
        if intent:
            return True
        return False


# Actual processes
def start(update, context):
    response = "I'm a bot, please talk to me!"

    log(update, response)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def greet(update, context):
    now = datetime.datetime.now()
    hour = now.hour
    speaker = update.message.chat.first_name

    if 6 <= hour < 12:
        response = 'Good Morning  {}'.format(speaker)
    elif 12 <= hour < 17:
        response = 'Good Afternoon {}'.format(speaker)
    elif 17 <= hour < 23:
        response = 'Good Evening  {}'.format(speaker)
    else:
        response = 'Good Night  {}'.format(speaker)

    log(update, response)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def respond_intent(update, context):
    response = "I am in an intent"

    intent = match_to_category(update.message, intents)
    if intent:
        response = random.choice(intent['responses'])

    log(update, response)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def unknown(update, context):
    response = "Sorry I did not understand that!"

    log(update, response)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)
