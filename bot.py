import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask

# ---------------- ENV VARIABLES ---------------- #
BOT_TOKEN = os.environ.get("BOT_TOKEN")  # Telegram bot token
PORT = int(os.environ.get("PORT", 10000))  # Render port

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
    "Kabhi party me jhoot bola? 🥳",
    "Sabse ajeeb hobby kya hai? 🎨",
    "Apna favourite movie scene batao 🎬",
    "Kabhi kisi ko impress karne ke liye exaggerate kiya? 😎",
    "Sabse funny nickname kya mila hai? 😂",
    "Kya kabhi late night khud se baatein ki? 🌙",
    "Sabse unusual fear kya hai? 👻",
    "Kya kabhi kisi friend ko secretly admire kiya? 💌",
    "Apni childhood crush ka naam batao 😏",
    "Kabhi kisi secret gift diya hai? 🎁"
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
    "Kisi se funny challenge karo 😜",
    "Next message sirf rhyming words me likho 🎤",
    "Ek random fact share karo 🧠",
    "Apna childhood secret batao 🍼",
    "Apni favorite joke batao 😂",
    "Kisi ek member ko hug emoji bhejo 🤗",
    "Apni worst habit batao 🤭",
    "Next message sirf questions me likho ❓",
    "Apni favorite snack batao 🍫",
    "Kisi ko funny nickname do 😎"
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
    truth_text = random.choice(TRUTHS)
    await update.message.reply_text(f"💬 Truth: {truth_text}")

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dare_text = random.choice(DARES)
    await update.message.reply_text(f"🎯 Dare: {dare_text}")

# ---------------- RELATION COMMAND ---------------- #
async def relation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    members = await context.bot.get_chat_administrators(chat.id)
    member_ids = [m.user.id for m in members if not m.user.is_bot]
    if len(member_ids) < 2:
        await update.message.reply_text("Not enough members in the group.")
        return

    user1, user2 = random.sample(member_ids, 2)
    rel = random.choice(RELATIONS)

    text = (
        f"✨ Aaj ka special connection ✨\n\n"
        f"{context.bot.get_chat_member(chat.id, user1).user.mention_html()} 💖 "
        f"aur {context.bot.get_chat_member(chat.id, user2).user.mention_html()} 💖\n\n"
        f"Unka relation hai: {rel} 🌹\n\n"
        "Dil se judi hui yeh dosti aur pyaar, "
        "har pal khushiyo se bhara rahe 💫\n"
        "💌 Chat me sabse cute aur special pair!"
    )

    await update.message.reply_text(text, parse_mode="HTML")

# ---------------- PAIR COMMAND ---------------- #
async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    admins = await context.bot.get_chat_administrators(chat.id)
    admin_ids = [a.user.id for a in admins if not a.user.is_bot]
    if len(admin_ids) < 2:
        await update.message.reply_text("Not enough admins to form a pair.")
        return

    admin1, admin2 = random.sample(admin_ids, 2)
    pair_name = random.choice(PAIR_NAMES)

    text = (
        f"👑 Admin Duo Spotlight 👑\n\n"
        f"{context.bot.get_chat_member(chat.id, admin1).user.mention_html()} ✨ "
        f"aur {context.bot.get_chat_member(chat.id, admin2).user.mention_html()} ✨\n\n"
        f"Unka magical pair: {pair_name} 💫\n\n"
        "Group ke is special duo ke saath, har chat aur har moment me masti aur pyaar 🌈\n"
        "🌟 Boss & Queen vibes always!"
    )

    await update.message.reply_text(text, parse_mode="HTML")

# ---------------- FLASK HEALTH CHECK ---------------- #
app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running!"

# ---------------- RUN BOT ---------------- #
if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("truth", truth))
    application.add_handler(CommandHandler("dare", dare))
    application.add_handler(CommandHandler("relation", relation))
    application.add_handler(CommandHandler("pair", pair))

    # Run Telegram polling in main thread
    application.run_polling(poll_interval=3)