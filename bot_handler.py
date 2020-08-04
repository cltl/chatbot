import os
import telegram
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter

CLTL_TOKEN = os.environ.get('CLTL_TOKEN')
greetings = ('hello', 'hi', 'greetings', 'sup')
toxic = ('stupid', 'moron')


# Tailor made filters
class FilterGreetings(BaseFilter):
    def filter(self, message):
        return message.text.lower() in greetings


class FilterToxic(BaseFilter):
    def filter(self, message):
        return message.text.lower() in toxic


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


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def main():
    # # Who am I?
    bot = telegram.Bot(token=CLTL_TOKEN)
    print(bot.get_me())

    # Instantiate filters
    filter_greetings = FilterGreetings()
    filter_toxic = FilterToxic()
    updater = Updater(token=CLTL_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Define handlers (order is important)
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    greet_handler = MessageHandler(filter_greetings, greet)
    dispatcher.add_handler(greet_handler)

    echo_handler = MessageHandler(filter_toxic, echo)
    dispatcher.add_handler(echo_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Run!
    updater.start_polling()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
