from bot_commands import *
from telegram.ext import ApplicationBuilder, CommandHandler


bot_token = ('7347498031:AAHyFgo712sWO0yEQc6uGhpA6CbfQxVZ3E0')

# bot_token = '7347498031:AAHyFgo712sWO0yEQc6uGhpA6CbfQxVZ3E0'

def main():
    if bot_token is None:
        print('Bot token not found. Please save your bot token in .env file under the name BOT_TOKEN')
        return

    application = ApplicationBuilder().token(bot_token).build()

    application.add_handler(CommandHandler('start', start_command))
    test = application.add_handler(CommandHandler('create', create))
    print("****************************")
    print(test)

    application.run_polling()


if __name__ == '__main__':
    main()