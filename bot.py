import logging
from decouple import config
from telegram.ext import Updater, CommandHandler
from modules.searches import (
    search_by_dni,
    search_by_name,
    search_by_second_name,
    search_by_lastname
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
bot_token = config('bot_token')
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


def send_many_messages(chat_id, context, messages):
    for message in messages:
        context.bot.send_message(
            chat_id=chat_id,
            text=message
        )


def search_dni(update, context):
    data = search_by_dni(context.args[0])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=data
    )


def search_name(update, context):
    data = search_by_name(context.args[0])
    if isinstance(data, list):
        send_many_messages(update.effective_chat.id, context, data)
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=data
        )


def search_second_name(update, context):
    data = search_by_second_name(context.args[0])
    if isinstance(data, list):
        send_many_messages(update.effective_chat.id, context, data)
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=data
        )


def search_lastname(update, context):
    data = search_by_lastname(context.args[0])
    if isinstance(data, list):
        send_many_messages(update.effective_chat.id, context, data)
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=data
        )


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Bienvenido wachin'
    )


def start_bot():
    start_handler = CommandHandler('start', start)
    search_dni_handler = CommandHandler('dni', search_dni)
    search_name_handler = CommandHandler('name', search_name)
    search_second_name_handler = CommandHandler(
        'second_name', search_second_name
    )
    search_lastname_handler = CommandHandler('lastname', search_lastname)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(search_dni_handler)
    dispatcher.add_handler(search_name_handler)
    dispatcher.add_handler(search_second_name_handler)
    dispatcher.add_handler(search_lastname_handler)


def run():
    start_bot()
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run()
