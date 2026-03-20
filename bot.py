import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Environment variable me set kiya hua token
TOKEN = os.getenv("TOKEN")

# ---------------- TRUTHS ----------------
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

# ---------------- DARES ----------------
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

# ---------------- RELATIONS ----------------
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

# ---------------- COMMAND FUNCTIONS ----------------
async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(TRUTHS))

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(DARES))

async def relation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    if chat.type not in ["group", "supergroup"]:
        await update.message.reply_text("Ye command sirf group me kaam karti hai ❌")
        return
    admins = await context.bot.get_chat_administrators(chat.id)
    users = [admin.user for admin in admins]
    if len(users) < 2:
        await update.message.reply_text("Group me kam se kam 2 admin hone chahiye 😅")
        return
    u1, u2 = random.sample(users, 2)
    relation = random.choice(RELATIONS)
    msg = (
        f"💞 Random Relation Found! 💞\n\n"
        f"👤 {u1.mention_html()} 🤝 {u2.mention_html()}\n"
        f"🔗 Relation: <b>{relation}</b>"
    )
    await update.message.reply_html(msg)

async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    if chat.type not in ["group", "supergroup"]:
        await update.message.reply_text("Ye command sirf group me kaam karti hai ❌")
        return
    members_count = await chat.get_member_count()
    if members_count < 2:
        await update.message.reply_text("Kam se kam 2 member hone chahiye 😅")
        return
    admins = await context.bot.get_chat_administrators(chat.id)
    users = [admin.user for admin in admins]
    if len(users) < 2:
        await update.message.reply_text("Kam se kam 2 admin hone chahiye 😅")
        return
    u1, u2 = random.sample(users, 2)
    pair_names = RELATIONS  # Same as relation list
    pair_name = random.choice(pair_names)
    msg = (
        "💘 Special Pair 💘\n\n"
        f"{u1.mention_html()} ❤️ {u2.mention_html()}\n\n"
        f"✨ <b>{pair_name}</b>"
    )
    await update.message.reply_html(msg)

# ---------------- RUN BOT ----------------
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("truth", truth))
    app.add_handler(CommandHandler("dare", dare))
    app.add_handler(CommandHandler("relation", relation))
    app.add_handler(CommandHandler("pair", pair))

    print("🤖 Bot is running...")
    # direct run_polling without asyncio.run
    app.run_polling()