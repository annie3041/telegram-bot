from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Функция, которая отвечает на команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я работаю 🙂")

# Создание приложения бота
app = ApplicationBuilder().token("YOUR_TELEGRAM_TOKEN").build()
app.add_handler(CommandHandler("start", start))

# Запуск бота
app.run_polling()