import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask

# ---------------- ENV VARIABLES ---------------- #
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ---------------- TRUTHS & DARES ---------------- #
TRUTHS = [
    "Sabse bada secret kya hai? 🤫",
    "Group me sabse zyada kaun pasand hai? 😏",
    "Kabhi kisi pe secret crush raha hai? 💘",
    "Pehli baar pyaar kab hua tha? 💕",
    "Last kis se chat ki thi? 📱",
    "Apni love life ek word me describe karo ❤️",
    "Kisi teacher se kabhi daant padi hai? 😅",
    "Exam ke time sabse zyada kya darr lagta hai? 📚",
    "Kabhi cheat kiya hai exam me? 😬",
    "Sabse embarrassing moment kya tha? 😳",
    "Kabhi kisi dost se jhoot bola hai? 🤥",
    "Group me sabse cute kaun lagta hai? 🥰",
    "One-sided love kabhi hua hai? 💔",
    "Late night jagne ka reason kya hota hai? 🌙",
    "Kisi pe abhi bhi crush hai? 😌",
    "Apni weakness kya maante ho? 🫣",
    "College/school ka best moment konsa tha? 🎓",
    "Kabhi kisi message ka screenshot liya hai? 📸",
    "Future me love marriage ya arrange? 💍",
    "Aaj ka mood honestly batao 😇"
]

DARES = [
    "Apna nickname batao 😎",
    "Group me 3 emojis bhejo 🔥😂💯",
    "Apni current feeling ek emoji me batao 😊",
    "Kisi ek member ko tag karke hi bolo 👋",
    "Next message ALL CAPS me likho 🗣",
    "Apna favourite song ka naam batao 🎵",
    "Kisi ko group me compliment do 💐",
    "Apni crush type describe karo 😏",
    "Aaj ka study goal batao 📖",
    "Group me ❤️ emoji bhejo",
    "Apna dream job batao 💼",
    "Last used emoji bhejo 😄",
    "Kisi ek word me apna nature batao 🌸",
    "Apna favourite movie ya web series batao 🎬",
    "Aaj ka mood ek sticker me bhejo 🧠",
    "Apni height ka guess batao 📏",
    "Apna favourite food ka naam likho 🍕",
    "Kisi ek member ke liye positive line likho ✨",
    "Apna favourite subject batao 📘",
    "Aaj ka time batao jab uthe the ⏰"
]

RELATIONS = [
    "🤝 Besties",
    "🖤 Toxic & Loyal",
    "😈 Devil & Angel",
    "👑 King & Killer Queen",
    "🐍 Snake & Charmer",
    "⚡ Thunder & Lightning",
    "😎 Boss & Queen",
    "🤪 Drama King & Queen",
    "🔥 Fire & Spark",
    "🐒 Monkey & Banana",
    "🍕 Pizza & Coke",
    "🎧 DJ & Listener",
    "💕 Love Birds",
    "💖 Soulmates",
    "💘 Heartbeat Duo",
    "💞 Forever Pair",
    "🌹 Rose & Thorn",
    "🌙 Moon & Star",
    "☀️ Sun & Sunshine",
    "Best Friends Forever 🤝",
    "Chill Buddy 😎",
    "Lucky Pair 🍀",
    "Study Partners 📚",
    "College Buddies 🎓",
    "Secret Supporters 🤫",
    "Power Duo 💪",
    "Dream Team 🌈"
]

PAIR_NAMES = [
    "🔥 Fire & Spark",
    "🌙 Moon & Star",
    "😎 Boss & Queen",
    "💘 Crush Couple",
    "✨ Golden Duo",
    "👑 King & Queen",
    "💞 Dil & Dhadkan",
    "🫶 Bestie Pair",
    "🤝 Besties",
    "MOTU AND PATLU",
    "🖤 Toxic & Loyal",
    "😈 Devil & Angel",
    "👑 King & Killer Queen",
    "🤪 Drama King & Queen",
    "🐒 Monkey & Banana",
    "🍕 Pizza & Coke",
    "🎧 DJ & Listener",
    "💕 Love Birds",
    "💖 Soulmates",
    "💘 Heartbeat Duo",
    "💞 Forever Pair",
    "🌹 Rose & Thorn",
    "☀️ Sun & Sunshine"
]

# ---------------- TELEGRAM HANDLERS ---------------- #
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Use /truth, /dare, /relation or /pair"
    )

async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(TRUTHS))

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(DARES))

async def relation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(RELATIONS))

async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(PAIR_NAMES))

# ---------------- FLASK + BOT ---------------- #
app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running!"

if __name__ == "__main__":
    # Telegram Bot application
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("truth", truth))
    application.add_handler(CommandHandler("dare", dare))
    application.add_handler(CommandHandler("relation", relation))
    application.add_handler(CommandHandler("pair", pair))

    # Run bot in polling mode
    import threading
    def run_bot():
        application.run_polling()

    threading.Thread(target=run_bot).start()
    # Run Flask app to keep Render happy
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))