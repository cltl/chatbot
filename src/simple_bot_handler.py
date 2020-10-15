import requests


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_messages(self, offset=None, timeout=200):
        """ Function to get all messages sent to the bot """
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        return resp.json()['result']

    def send_message_to(self, chat_id, text):
        """ Function to send a message from the bot to a specific user"""
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_message_by(self, chat_id):
        """ Function to get the last message sent to the bot by a specific user"""
        messages = self.get_messages()
        messages_by_user = list(filter(lambda d: d['message']['chat']['id'] == chat_id, messages))

        if messages_by_user:
            last_message = messages_by_user[-1]
        else:
            last_message = []

        return last_message
