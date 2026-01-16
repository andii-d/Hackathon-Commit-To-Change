"""
BOT NAME: credo
BOT USERNAME: credoAIBot
LINK: t.me/credoAIBot
"""

import asyncio
import os
import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from openai import OpenAI
from dotenv import load_dotenv


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Tell me a habit you completed.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    await update.message.reply_text("Got it. Thinking...")

    client = context.application.bot_data["openai_client"]
    try:
        response = await asyncio.to_thread(
            client.responses.create,
            model="gpt-4o-mini",
            input=(
                "You are a supportive habit coach. Reply in one short sentence. "
                f"User message: {text}"
            ),
        )
        reply = response.output_text.strip() or "Great job! Keep it up!"
        await update.message.reply_text(reply)
    except Exception as exc:
        logging.exception("OpenAI request failed: %s", exc)
        await update.message.reply_text(
            "Sorry, I had trouble reaching the AI. Try again in a moment."
        )


def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    telegram_token = os.environ["TELEGRAM_BOT_TOKEN"]
    openai_key = os.environ["OPENAI_API_KEY"]

    app = ApplicationBuilder().token(telegram_token).build()
    app.bot_data["openai_client"] = OpenAI(api_key=openai_key)
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()


if __name__ == "__main__":
    main()
