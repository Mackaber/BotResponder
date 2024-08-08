import asyncio
import json
import os
import traceback

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes
from telegram.ext.filters import MessageFilter

from langtale import langtail_request

bot_app = ApplicationBuilder().token(os.getenv('TELEGRAM_TOKEN')).build()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello to hell {update.effective_user.first_name}')

async def message_repeater(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)
    
async def langtale_responder(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = langtail_request(update.message.text)
    await update.message.reply_text(response)

class TextMessageFilter(MessageFilter):
    def filter(self, message):
        return message.text and not message.text.startswith('/')

# Instantiate the filter
text_message_filter = TextMessageFilter()

bot_app.add_handler(CommandHandler("hello", hello))
# bot_app.add_handler(MessageHandler(text_message_filter, message_repeater))
bot_app.add_handler(MessageHandler(text_message_filter, langtale_responder))


async def tg_bot_main(bot_app, event):
    async with bot_app:
        await bot_app.process_update(
            Update.de_json(json.loads(event["body"]), bot_app.bot)
        )

def lambda_handler(event, context):
    try:
        print(event)
        print(context)
        # DISABLED!
        # asyncio.run(tg_bot_main(bot_app, event)) 
    except Exception as e:
        traceback.print_exc()
        print(e)
        return {"statusCode": 500}

    return {"statusCode": 200}