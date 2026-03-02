from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Tu token de BotFather
TOKEN = "8701174108:AAGCEId4i2BXdVUcpDv7DyHRjXml4pv6Wt0"

# Función que maneja el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛸 ¡Hola! Soy AiFucito, tu asistente ufológico.\n"
        "Envía tus reportes de avistamientos y yo los organizaré para ti."
    )

# Construir la aplicación y añadir el handler
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Ejecutar el bot
if __name__ == "__main__":
    print("Bot iniciado correctamente...")
    app.run_polling()
