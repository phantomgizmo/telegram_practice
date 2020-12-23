import sys
import inspect
from typing import Optional
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ardi entog")

def sendPhoto(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo="https://p.bigstockphoto.com/GeFvQkBbSLaMdpKXF1Zv_bigstock-Aerial-View-Of-Blue-Lakes-And--227291596.jpg")

def sendUserPhoto(update, context):
    """Return photo sent by user."""
    # file_id = context.bot.getFile(update.message.photo[-1].file_id)
    # file_id = update.message.photo[-1].file_id
    file_id = update.effective_message.photo[-1].file_id

    context.bot.send_photo(chat_id=update.effective_chat.id, photo=file_id)

def getCommandHandler(command_name: str, function_name: str) -> Optional[CommandHandler]:
    fun = getFun(function_name)

    if fun: return CommandHandler(command_name, fun) 
    else: return None

def getMessageHandler(function_name: str) -> Optional[MessageHandler]:
    fun = getFun(function_name)

    if fun: return MessageHandler(Filters.photo & Filters.caption_regex(r'Process'), fun)
    else: return None


def getFun(function_name: str):
    funcmembers = inspect.getmembers(sys.modules[__name__], inspect.isfunction) #get all function in current context
    funcmembers = {key: fun for key, fun in funcmembers} #map tuple of (key, func) to a dict

    fun = funcmembers.get(function_name)

    if fun: return fun
    else: return None