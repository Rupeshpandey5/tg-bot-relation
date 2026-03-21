import os
import random
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread

# ---------------- ENV VARIABLES ---------------- #
BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

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
    "🤝 Besties", "🖤 Toxic & Loyal", "😈 Devil & Angel",
    "👑 King & Killer Queen", "🐍 Snake & Charmer", "⚡ Thunder & Lightning",
    "😎 Boss & Queen", "🤪 Drama King & Queen", "🔥 Fire & Spark",
    "🐒 Monkey & Banana", "🍕 Pizza & Coke", "🎧 DJ & Listener",
    "💕 Love Birds", "💖 Soulmates", "💘 Heartbeat Duo",
    "💞 Forever Pair", "🌹 Rose & Thorn", "🌙 Moon & Star",
    "☀️ Sun & Sunshine", "Best Friends Forever 🤝"
]

PAIR_NAMES = [
    "🔥 Fire & Spark", "🌙 Moon & Star", "😎 Boss & Queen",
    "💘 Crush Couple", "✨ Golden Duo", "👑 King & Queen",
    "💞 Dil & Dhadkan", "🫶 Bestie Pair", "🤝 Besties",
    "🖤 Toxic & Loyal", "😈 Devil & Angel", "👑 King & Killer Queen"
]

# ---------------- TELEGRAM COMMANDS ---------------- #
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Use /truth, /dare, /relation or /pair"
    )

async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(TRUTHS))

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(DARES))

async def relation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    members = await context.bot.get_chat_administrators(chat.id)
    member_ids = [m.user.id for m in members if not m.user.is_bot]
    if len(member_ids) < 2:
        await update.message.reply_text("Not enough members in the group.")
        return
    user1, user2 = random.sample(member_ids, 2)
    rel = random.choice(RELATIONS)
    await update.message.reply_text(
        f"{context.bot.get_chat_member(chat.id, user1).user.mention_html()} ❤️ "
        f"{context.bot.get_chat_member(chat.id, user2).user.mention_html()} = {rel}",
        parse_mode="HTML"
    )

async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    admins = await context.bot.get_chat_administrators(chat.id)
    admin_ids = [a.user.id for a in admins if not a.user.is_bot]
    if len(admin_ids) < 2:
        await update.message.reply_text("Not enough admins to form a pair.")
        return
    admin1, admin2 = random.sample(admin_ids, 2)
    pair_name = random.choice(PAIR_NAMES)
    await update.message.reply_text(
        f"{context.bot.get_chat_member(chat.id, admin1).user.mention_html()} + "
        f"{context.bot.get_chat_member(chat.id, admin2).user.mention_html()} = {pair_name}",
        parse_mode="HTML"
    )

# ---------------- FLASK HEALTH CHECK ---------------- #
app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running!"

# ---------------- RUN BOT & FLASK ---------------- #
def run_flask():
    app.run(host="0.0.0.0", port=PORT)

def run_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("truth", truth))
    application.add_handler(CommandHandler("dare", dare))
    application.add_handler(CommandHandler("relation", relation))
    application.add_handler(CommandHandler("pair", pair))
    application.run_polling()

if __name__ == "__main__":
    # Flask runs in separate thread for Render health check
    Thread(target=run_flask).start()
    # Telegram bot runs in main thread
    run_bot()