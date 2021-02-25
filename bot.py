import logging
from decouple import config
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from modules.searches import (
    search_by_dni,
    search_by_name,
    search_by_second_name,
    search_by_lastname,
    search_by_second_lastname,
    search_by_name_and_lastname,
    search_by_expression,
    search_picture
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
bot_token = config('bot_token')
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


def send_picture(update, context, data):
    dni = data.split('\n')[1]
    url = search_picture(dni)
    if url:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)


def send_many_messages(update, context, messages):
    for message in messages:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message
        )

    if len(messages) == 1:
        send_picture(update, context, data=messages[0])


def process_data(update, context, data):
    if isinstance(data, dict):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=data['message']
        )

    else:
        send_many_messages(update, context, data)


def search_dni(update, context):
    data = search_by_dni(context.args[0])
    if isinstance(data, str):
        data = [data]

    process_data(update, context, data)


def search_name(update, context):
    data = search_by_name(context.args[0])
    process_data(update, context, data)


def search_second_name(update, context):
    data = search_by_second_name(context.args[0])
    process_data(update, context, data)


def search_lastname(update, context):
    data = search_by_lastname(context.args[0])
    process_data(update, context, data)


def search_second_lastname(update, context):
    data = search_by_second_lastname(context.args[0])
    process_data(update, context, data)


def search_name_lastname(update, context):
    data = search_by_name_and_lastname(context.args[0], context.args[1])
    process_data(update, context, data)


def search_expression(update, context):
    if update.message.text.isnumeric():
        data = search_by_dni(update.message.text)
        if isinstance(data, str):
            data = [data]

        process_data(update, context, data)

    else:
        accuracy = len(update.message.text.split(' '))
        data = search_by_expression(update.message.text, accuracy)
        process_data(update, context, data)


def start(update, context):
    with open('greet.txt', 'r') as file:
        bot_greet = file.read()
    
    username = update.message.from_user['first_name']
    user_greet = f'Hola {username} 😺'
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='\n'.join([user_greet, bot_greet])
    )


def start_bot():
    start_handler = CommandHandler('start', start)
    search_dni_handler = CommandHandler('ci', search_dni)
    search_name_handler = CommandHandler('nombre', search_name)
    search_second_name_handler = CommandHandler(
        'segundo_nombre',
        search_second_name
    )
    search_lastname_handler = CommandHandler('apellido', search_lastname)
    search_second_lastname_handler = CommandHandler(
        'segundo_apellido',
        search_second_lastname
    )
    search_name_lastname_handler = CommandHandler(
        'nombre_apellido',
        search_name_lastname
    )
    text_handler = MessageHandler(Filters.text, search_expression)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(search_dni_handler)
    dispatcher.add_handler(search_name_handler)
    dispatcher.add_handler(search_second_name_handler)
    dispatcher.add_handler(search_lastname_handler)
    dispatcher.add_handler(search_second_lastname_handler)
    dispatcher.add_handler(search_name_lastname_handler)
    dispatcher.add_handler(text_handler)


def run():
    start_bot()
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run()
