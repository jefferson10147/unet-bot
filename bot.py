import logging
from decouple import config
from telegram.ext import Updater, CommandHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
bot_token = config('bot_token')
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Bienvenido wachin'
    )


def start_bot():
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)


def run():
    start_bot()
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run()
