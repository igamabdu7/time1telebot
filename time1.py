import os
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

now = datetime.now()

strNow = now.strftime("%d.%m.%Y  %H:%M:%S")

def start (update, context):
    update.message.reply_text("HI!")

def time(update, context):
    update.message.reply_text("Time is "+strNow)
def echo(update, context):
    update.message.reply_text(update.message.text)
def main():
    TOKEN='5589136382:AAGc5BvasKO3853gCedlPn-_qqcHLi_E5Mc'
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("time",time))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
