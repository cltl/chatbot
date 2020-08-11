import os
import json


def read_token():
    TOKENS_PATH = os.path.join(os.path.dirname(__file__), '../resources/tokens.json')
    with open(TOKENS_PATH) as f:
        TOKENS = json.load(f)

    return TOKENS['CLTL_token']


def read_intents():
    INTENTS_PATH = os.path.join(os.path.dirname(__file__), '../resources/intents.json')
    with open(INTENTS_PATH) as f:
        INTENTS = json.load(f)

    return INTENTS
