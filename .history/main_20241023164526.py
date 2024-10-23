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
