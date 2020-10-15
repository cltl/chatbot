# CLTL chatbot

This repository contains the basic structure for a Telegram chatbot.


## Installation 
To run this code you will need Python 3. We strongly recommend using some sort of virtual environment manager, for example Anaconda. To install all the required dependencies you can run:

```
pip install -r requirements.txt
```

You will also need to add a file under the ```resources``` folder called ```tokens.json``` as such:

```json
{
  "CLTL_token": "YOUR_TOKEN_XXX"
}
```

The CLTL token may be shared on demand, or you can create your own bot following these [instructions](https://core.telegram.org/bots#3-how-do-i-create-a-bot).


## Running
To run the chatbot, you can run the ```main.py``` script. Then you will be able to chat with the CLTL bot: t.me/cltl_bot on telegram (either mobile or the desktop app). 

## Testing and developing 

### Preset Q/A
The easiest way to edit this ot is to go to the ```intents.json``` file and add the series of predefined Q/A you want the chatbot to work with.

### Filters and MessageHandlers
If you want to explore the Telegram functionality further, you can take a look at the ```bot_handler.py``` script.

You should override the ```BaseFilter``` class to create your own filters and determine which types of messages your bot should react to. 
After this, you can implement a function that determines which response should be given to this type of messages.

For an example, you can look at the ```filter_greetings``` class and the ```greet_handler``` function on the ```bot_handler.py``` file, and the way they are called on ```main.py```.


