from telegram.ext import Updater
from command.getAppHandler import getCommandHandler
from command.getAppHandler import getMessageHandler

from helpers.accesss_env import access_env

TOKEN = access_env("BOT_TOKEN") #get token from dotenv

updater = Updater(token=TOKEN, use_context=True) #create updater instance
dispatcher = updater.dispatcher

start_handler = getCommandHandler('start', 'start')

sendPhoto_handler = getCommandHandler('send_photo', 'sendPhoto')

sendUserPhoto_handler = getMessageHandler('send_user_photo', 'sendUserPhoto')

processPhoto_handler = getMessageHandler('process_photo', 'processPhoto')

dispatcher.add_handler(start_handler)
dispatcher.add_handler(sendPhoto_handler)
dispatcher.add_handler(sendUserPhoto_handler)
dispatcher.add_handler(processPhoto_handler)

if __name__ == '__main__':
    updater.start_polling()