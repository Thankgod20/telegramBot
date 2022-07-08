from urllib import response
import Constant as Keys
from telegram.ext import *
import Response as R
import json 

print("Bot Started")

def start_command(update,context):
    update.message.reply_text("lets Interract")

def help_command(update,context):
    f = open("../help.json")
    data = json.load(f)
    update.message.reply_text(data['help'])

def handle_message(update,context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)

    update.message.reply_text(response)

def error(update,context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(Keys.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(2)
    updater.idle()
main()
