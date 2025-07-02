from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from urllib.parse import urlparse
from bypass import BYPASS_HANDLERS, generic_bypass
import os

def get_domain(url):
    return urlparse(url).netloc.replace("www.", "")

def route_bypass(url):
    domain = get_domain(url)
    bypass_func = BYPASS_HANDLERS.get(domain, generic_bypass)
    return bypass_func(url)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Send me a shortened link and I'll bypass it!")

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.startswith("http"):
        await update.message.reply_text("⏳ Bypassing...")
        result = route_bypass(text)
        await update.message.reply_text(f"🔗 Bypassed: {result}")
    else:
        await update.message.reply_text("❌ Please send a valid URL.")

if __name__ == "__main__":
    BOT_TOKEN = os.getenv("7494439315:AAEKj2V2qMi3BO3SQSlWoeGCLUqGiZ1GLXE") or "YOUR_BOT_TOKEN_HERE"
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    print("🚀 Bypass Pro Bot is running...")
    app.run_polling()
