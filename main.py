from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from urllib.parse import urlparse
from bypass import BYPASS_HANDLERS, generic_bypass

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Send me any shortened URL and I’ll try to bypass it!")

def get_domain(url):
    return urlparse(url).netloc.replace("www.", "")

def route_bypass(url):
    domain = get_domain(url)
    bypass_func = BYPASS_HANDLERS.get(domain, generic_bypass)
    return bypass_func(url)

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "http" in text:
        await update.message.reply_text("⏳ Bypassing, please wait...")
        result = route_bypass(text)
        await update.message.reply_text(f"🔗 Bypassed: {result}")
    else:
        await update.message.reply_text("❌ Please send a valid URL.")

if __name__ == "__main__":
    import os

    BOT_TOKEN = os.getenv("BOT_TOKEN") or "YOUR_BOT_TOKEN"

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

    print("🚀 Bypass Pro Bot is running...")
    app.run_polling()
