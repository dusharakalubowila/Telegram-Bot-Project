import json
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace with your bot's token
BOT_TOKEN = "8093290779:AAHU_dRjaGfqc18C7XLXzOQLw7ywLOTcMms"

# Replace with your private channel ID
CHANNEL_ID = "-1002209251849"

# Load content map from JSON file (or database)
def load_content_map():
    with open('content.json', 'r') as file:
        return json.load(file)

# Start command handler
async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    args = context.args  # Get arguments passed with the /start command

    if not args:
        await update.message.reply_text("Welcome! Use /start <content_id> to access content. Example: /start 1")
        return

    content_id = args[0]
    content_map = load_content_map()

    if content_id in content_map:
        message_id = content_map[content_id]
        await context.bot.forward_message(
            chat_id=user_id,
            from_chat_id=CHANNEL_ID,
            message_id=message_id
        )
        await update.message.reply_text("Here is your requested content!")
    else:
        await update.message.reply_text(f"Invalid content ID: {content_id}. Try another ID.")

# Main function to run the bot
def main():
    # Initialize the Application with the bot token
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    application.run_polling()
    print("Bot is running...")

if __name__ == "__main__":
    main()
