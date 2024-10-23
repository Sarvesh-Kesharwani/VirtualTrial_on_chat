from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("yisol/IDM-VTON")
prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]


from typing import Final 
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7709502643:AAHtbgPqzYvJjkWly3dGhf7zAFKvztfRUYs'
bot_username: Final = '@VirtualTrial_sark42_bot'

# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to Virtual Trial Bot!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('plz type smth so i can respond to u!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('this is a custom command!')

# responses

def handle_response(txt: str) -> str:
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

    print(f'User ({update.message.chat.id}) in {message_type}: "{}"')