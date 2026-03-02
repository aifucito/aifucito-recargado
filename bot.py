from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8701174108:AAGCEId4i2BXdVUcpDv7DyHRjXml4pv6Wt0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛸 ¡Hola! Soy AiFucito, tu asistente ufológico. "
        "Envía tus reportes de avistamientos y yo los organizaré para ti."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    print("Bot iniciado correctamente...")
    app.run_polling()
