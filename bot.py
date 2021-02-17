import logging
from decouple import config
from telegram.ext import Updater, CommandHandler
from modules.searches import search_by_dni


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
bot_token = config('bot_token')
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


def search_dni(update, context):
    student = search_by_dni(context.args[0])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=student.show_data()
    )


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Bienvenido wachin'
    )


def start_bot():
    start_handler = CommandHandler('start', start)
    search_dni_handler = CommandHandler('dni', search_dni)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(search_dni_handler)


def run():
    start_bot()
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run()
