import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
updater = Updater(token='666388885:AAH3H0FxJgz48dOa8kV-gXbGLC-9-oeLrz0')
#dispatcher = updater.dispatcher


logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



def start (bot, update):
 bot.send_message (chat_id = update.message.chat_id, text = 'hi creator im working')


#start_handler = CommandHandler ('start', start)


#dispatcher.add_handler (start_handler)

updater.start_polling(poll_interval = 1.0,timeout=20)

updater.idle()