import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from src.bot_handler import *


def main():
    # Who am I?
    bot = telegram.Bot(token=CLTL_TOKEN)
    print(bot.get_me())

    # Instantiate filters
    filter_greetings = FilterGreetings()
    filter_intent = FilterIntents()

    # Basic telegram functionality for updates
    updater = Updater(token=CLTL_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Define handlers (order is important)
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    greet_handler = MessageHandler(filter_greetings, greet)
    dispatcher.add_handler(greet_handler)

    intents_handler = MessageHandler(filter_intent, respond_intent)
    dispatcher.add_handler(intents_handler)

    unknown_handler = MessageHandler(Filters.all, unknown)
    dispatcher.add_handler(unknown_handler)

    # Run!
    updater.start_polling()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
