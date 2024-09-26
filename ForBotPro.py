from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def check_username(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Yangi foydalanuvchi haqida ma'lumot
    for member in update.message.new_chat_members:
        username = member.username
        
        # Agar username 'bot' so'zini o'z ichiga olsa
        if username and 'bot' in username.lower():
            await context.bot.ban_chat_member(chat_id=update.effective_chat.id, user_id=member.id)
            await update.message.reply_text(f"{username} botlar guruhga qo'shilishi mumkin emas!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Salom! Bot ishlamoqda!")

if __name__ == "__main__":
    application = ApplicationBuilder().token("8012323632:AAG1EipaDBQwzbXijFJfyfMv1y1qLGwxY7E").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, check_username))

    application.run_polling()
