import os
import json


def read_token():
    tokens_path = os.path.join(os.path.dirname(__file__), '../resources/tokens.json')
    with open(tokens_path) as f:
        tokens = json.load(f)

    return tokens['CLTL_token']


def read_intents():
    intents_path = os.path.join(os.path.dirname(__file__), '../resources/hlt_qa.json')
    with open(intents_path) as f:
        intents = json.load(f)

    return intents


def log(update, response):
    speaker = update.message.chat.first_name
    message = update.message.text

    print("Received({speaker}): {message}".format(speaker=speaker, message=message))
    print("Responded: {response}\n".format(response=response))


def match_to_category(message, intents):
    clean_message = message.text.lower()

    for i in intents['intents']:
        questions = [q.lower() for q in i['questions']]

        if clean_message in questions:
            print("Type of intent is: {}".format(i["category"]))
            return i

    return None
