import os
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Get the Telegram API token from the environment variable
telegram_token = os.environ.get('TELEGRAM_TOKEN')

# Get the Mail.tm API key from the environment variable
mail_api_key = os.environ.get('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2ODI4NzA2MTksInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJ1c2VybmFtZSI6InNpaHNia2R0dG96ekBidWdmb28uY29tIiwiaWQiOiI2NDMzMTM5MGM5OWY5NGMwMGIzODA0ODUiLCJtZXJjdXJlIjp7InN1YnNjcmliZSI6WyIvYWNjb3VudHMvNjQzMzEzOTBjOTlmOTRjMDBiMzgwNDg1Il19fQ.hesHvDBUN-LHrELIWNXlwlfxDrXddUZOBIWawPpvGCJ0JM_514LNdCXsbyYQT23hEhmqt2nOkE-kxhGaYxUcDQ')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my temp mail bot! Send me a message and I'll forward it to your temporary email address.")

def handle_message(update, context):
    # Get the email address from the mail.tm API
    response = requests.post('https://api.mail.tm/accounts', headers={
        'Authorization': f'Bearer {mail_api_key}',
        'Content-Type': 'application/json'
    }, json={'password': 'your_password_here'})

    if response.status_code == 201:
        data = response.json()
        email_address = data['address']
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your temporary email address is {email_address}. Send a message to this address and it will be forwarded to you.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Failed to create email address")

# Set up the bot
updater = Updater(telegram_token, use_context=True)
dispatcher = updater.dispatcher

# Add command handlers
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

if __name__ == '__main__':
    # Start the bot
    updater.start_polling()
