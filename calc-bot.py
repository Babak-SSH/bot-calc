#!/.local/lib/python3.6
# -*- coding: utf-8 -*-

import urllib3
from telegram.ext import CommandHandler,Updater,MessageHandler,Filters
import logging


logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',level = logging.INFO)

logger = logging.getLogger(__name__)


def start_command(bot, Update):
    print(":)!")
    update.message.reply_text('it is working!!!')


def main():
    updater = Updater("679603790:AAGHUr0nnh6Ki7CkfCyOvRR-cU5uxJATsIc")

    d = updater.dispatcher

    d.add_handler(CommandHandler("start",start_command))

    updater.start_polling()

    updater.idle


if __name__ == "__main__":
    main()
# Keep the program running.
#while 1:
 #   time.sleep(10)
