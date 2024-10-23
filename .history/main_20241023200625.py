from typing import Final 
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os 

TOKEN: Final = '7709502643:AAHtbgPqzYvJjkWly3dGhf7zAFKvztfRUYs'
bot_username: Final = '@VirtualTrial_sark42_bot'
DOWNLOAD_PATH: Final = r'./downloads/'

# Create the directory if it doesn't exist
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)


# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to Virtual Trial Bot!')
    await update.message.reply_text('Welcome! Send me an image and I will fetch it.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Send')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('this is a custom command!')

# Handler to fetch and download images
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the list of photos sent in the message
    photo = update.message.photo[-1]  # Get the highest resolution image
    file_id = photo.file_id  # Get file ID of the photo

    # Fetch the file
    file = await context.bot.get_file(file_id)
    
    # Download the image to the specified path
    file_path = os.path.join(DOWNLOAD_PATH, f"{file_id}.jpg")
    await file.download_to_drive(file_path)

    # Confirm to the user
    await update.message.reply_text(f"Image received and saved as {file_path}")

# responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello! How can I help you?'
    if 'how are you' in processed:
        return 'I am fine, thank you! How are you?'
    if 'i love python' in processed:
        return 'I love python too!'
    return 'I am sorry, I do not understand you!'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    response: str = handle_response(text)

    print('Bot: ', response)
    await update.message.reply_text(response)

# error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Photo handler
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    # errors
    app.add_error_handler(error)

    # pools the bot
    print('Polling...')
    app.run_polling(poll_interval=3, timeout=20)