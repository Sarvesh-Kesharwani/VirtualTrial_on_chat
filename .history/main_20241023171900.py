# from diffusers import DiffusionPipeline

# pipe = DiffusionPipeline.from_pretrained("yisol/IDM-VTON")
# prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
# image = pipe(prompt).images[0]
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = 'YOUR_TELEGRAM_BOT_TOKEN'
bot_username: Final = '@VirtualTrial_sark42_bot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to Virtual Trial Bot!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Please type something so I can respond to you!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

# Responses
def handle_response(txt: str) -> str:
    processed: str = txt.lower()

    if 'hello' in processed:
        return 'Hello! How can I help you?'
    if 'how are you' in processed:
        return 'I am fine, thank you! How are you?'
    if 'i love python' in processed:
        return 'I love Python too!'
    return 'I am sorry, I do not understand you!'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

# Error Handling
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3, timeout=20)
