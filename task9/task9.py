
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )
#не работает с голосовыми и видео сообщениями, а также файлами, в жопу надоело
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if update.message.sticker:
        await update.message.reply_text(f'Your ID: {user.id}\nYour Name: {user.first_name} {user.last_name}')
        await update.message.reply_sticker(update.message.sticker)
    elif update.message.audio:
        await update.message.reply_text(f'Your ID: {user.id}\nYour Name: {user.first_name} {user.last_name}')
        await update.message.reply_audio(update.message.audio[-1])
    elif update.message.video:
        await update.message.reply_text(f'Your ID: {user.id}\nYour Name: {user.first_name} {user.last_name}')
        await update.message.reply_video(update.message.video)
    elif update.message.photo:
        await update.message.reply_text(f'Your ID: {user.id}\nYour Name: {user.first_name} {user.last_name}')
        await update.message.reply_photo(update.message.photo[-1])
    else:
        await update.message.reply_text(f'Your ID: {user.id}\nYour Name: {user.first_name} {user.last_name}\n{update.message.text}')

def main() -> None:
    """Start the bot."""
    application = Application.builder().token("5198156020:AAGobnTpL1rdEBY0Z85pWufWh5gmKJCvIMI").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, echo))
    application.run_polling()

if __name__ == "__main__":
    main()