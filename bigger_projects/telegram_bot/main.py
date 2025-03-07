from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# confidential
TOKEN: Final[str] = 'TOKEN_TO_FILL'
BOT_USERNAME: Final[str] = "<bot_username_to_fill"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello there, nice to meet you, let's chat")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text("Just type something and i will respond")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("just a custom command")

def handle_response(text: str) -> str:
    processed: str = text.lower()
    if "hello" in processed:
        return "Hey there !"
    if "how are you" in processed:
        return "good! thanks !"
    if "i love python" in processed:
        return "python is cooool !"
    else:
        return "i do not understand"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f"User '{update.message.chat.id}) in {message_type}: {text} ")
    if message_type in "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("Bot: ", response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"{update} caused error: {context.error}")

def main():
    print("starting up the bot...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)
    print("Polling...")
    app.run_polling(poll_interval=5)

if __name__ == "__main__":
    main()
