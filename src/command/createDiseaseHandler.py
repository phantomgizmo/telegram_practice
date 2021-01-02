from telegram.ext import CommandHandler
from telegram import Update
from telegram.ext import CallbackContext

from typing import Callable, Union

def createDiseaseCallback(disease_desc: str) -> Callable[[Union[str, Update], CallbackContext], any]:
    def diseaseCallback(update: Union[str, Update], context: CallbackContext) -> any:
        context.bot.send_message(chat_id=update.effective_chat.id, text=disease_desc)

        return 0

    return diseaseCallback

def createDiseaseHandler(disease_name: str, disease_desc: str) -> CommandHandler:
    diseaseCallback = createDiseaseCallback(disease_desc)
    return CommandHandler(disease_name, diseaseCallback)