import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ---------------- TRUTH (20) ---------------- #
TRUTHS = [
"Sabse bada secret kya hai? 🤫",
"Kisi pe crush hai? 😏",
"Last kis se chat ki thi? 📱",
"Pehla pyaar kab hua? 💕",
"Sabse embarrassing moment? 😳",
"Kabhi jhoot pakda gaya? 😅",
"Kisi ko propose kiya? 💘",
"Favorite person kaun hai? ❤️",
"Kabhi heartbreak hua? 💔",
"Apni love life describe karo 😆",
"Kisi se jalte ho? 😏",
"Kabhi kisi ko ignore kiya? 🙄",
"Kabhi roye ho kisi ke liye? 😢",
"Kisi ka phone check kiya? 📲",
"Kabhi cheat kiya exam me? 📚",
"Kisi ko secretly stalk karte ho? 👀",
"Sabse zyada kispe trust hai? 🤝",
"Kabhi kisi ko block kiya? 🚫",
"Kisi se abhi bhi pyaar hai? 💞",
"Apna biggest fear kya hai? 😨"
"Aapne sabse ajeeb sapna kab dekha?",
"Aapne apni life me sabse embarrassing moment kya tha?",
"Aapne kab kisi ko chupke se like kiya tha?",
"Aapka first crush kaun tha?",
"Aapne sabse bada jhoot kab bola?",
"Aapki koi aisi habit jo sabko irritate karti ho?",
"Aapne apni life me kab kisi ko hurt kiya?",
"Aapne kab kisi secret ko leak kiya?",
"Aapko sabse zyada jealousy kab mehsoos hui?",
"Aapka favorite childhood memory kya hai?",
"Aapne kab kisi ke liye kuch acha kiya bina wajah?",
"Aapki life me sabse crazy moment kya tha?",
"Aapne kab kisi ko silently admire kiya?",
"Aapne sabse weird food combination kab try kiya?",
"Aapka sabse bada fear kya hai?",
"Aapka favorite hobby kya hai?",
"Aapne kab kisi se sorry bola without meaning it?",
"Aapki hidden talent kya hai?",
"Aapne kab kisi ke saath overreact kiya?",
"Aapki dream destination kahaan hai?"
]

# ---------------- DARE (20) ---------------- #
DARES = [
"Group me 3 emojis bhejo 😂🔥😎",
"Kisi ko tag karke hi bolo 👋",
"Apna nickname batao 😆",
"Next msg ALL CAPS me likho 🗣",
"Kisi ko compliment do 💐",
"Apni crush type batao 😏",
"❤️ emoji bhejo group me",
"Apna fav song batao 🎵",
"Kisi ko good night bolo 🌙",
"Kisi ko roast karo 😈",
"Ek funny line likho 🤣",
"Kisi ko best friend bolo 🤝",
"Apni pic bhejo (optional 😜)",
"Kisi ka naam spam karo 😂",
"Kisi ko propose style msg bhejo 💘",
"Kisi ka status copy karo 😎",
"Kisi ko 'I miss you' bolo 😢",
"Kisi ko 'I love you' bolo 😍",
"Apni feeling emoji me batao 😊",
"Kisi ek ko hero bana do 👑"
]

# ---------------- RELATION (30) ---------------- #
RELATIONS = [
"💖 Soulmates", "💕 Love Birds", "💞 Perfect Couple", "🔥 Fire & Spark",
"🌙 Moon & Star", "☀️ Sun & Shine", "💘 Crush Goals", "😍 Cute Couple",
"😈 Devil & Angel", "🖤 Toxic & Loyal", "👑 King & Queen",
"🎧 DJ & Listener", "🍕 Pizza & Coke", "🐒 Monkey & Banana",
"🌹 Rose & Thorn", "⚡ Thunder & Lightning", "💓 Heartbeat Duo",
"🤝 Best Friends", "👀 Secret Lovers", "💫 Dream Pair",
"💎 Precious Bond", "🌈 Rainbow Pair", "💋 Kiss Couple",
"🎯 Perfect Match", "🫶 Forever Together", "🔥 Hot Couple",
"😎 Stylish Duo", "🥰 Made For Each Other", "💌 Hidden Love",
"💝 Special Connection"
]

# ---------------- PAIR (30) ---------------- #
PAIRS = [
"👑 Royal Pair", "🔥 Power Couple", "💖 Dream Couple", "😎 Cool Duo",
"💞 Love Connection", "💘 Perfect Match", "✨ Golden Pair",
"🌙 Night Couple", "☀️ Sunshine Duo", "🎯 Exact Match",
"🖤 Dark Love", "💓 Heart Pair", "💋 Kiss Duo",
"💎 Diamond Pair", "🫶 True Bond", "💫 Star Couple",
"🔥 Fire Duo", "😍 Cute Pair", "🥰 Lovely Couple",
"🎧 Music Pair", "🍫 Sweet Duo", "⚡ Energy Pair",
"👀 Secret Pair", "💝 Special Duo", "🤝 Best Duo",
"💌 Love Duo", "😈 Crazy Pair", "👑 King Duo",
"🌈 Colorful Pair", "💥 Blast Pair"
]

# ---------------- COMMANDS ---------------- #
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Bot Ready!\n\nCommands:\n/truth\n/dare\n/relation\n/pair"
    )

async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🧠 Truth:\n{random.choice(TRUTHS)}")

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🎯 Dare:\n{random.choice(DARES)}")

# ---------------- RELATION ---------------- #
async def relation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    members = await context.bot.get_chat_administrators(chat.id)

    users = [m.user for m in members if not m.user.is_bot]

    if len(users) < 2:
        await update.message.reply_text("Group me kam members hai 😅")
        return

    u1, u2 = random.sample(users, 2)
    rel = random.choice(RELATIONS)

    text = f"""
💖 {u1.mention_html()} ❤️ {u2.mention_html()} 💖

✨ Relation: {rel}

💌 Shayari:
"Do dil mile hai aaj yaha,
Kismat ne likha ek naya jaha 💫"
"""

    await update.message.reply_text(text, parse_mode="HTML")

# ---------------- PAIR ---------------- #
async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    admins = await context.bot.get_chat_administrators(chat.id)

    users = [a.user for a in admins if not a.user.is_bot]

    if len(users) < 2:
        await update.message.reply_text("Admins kam hai 😅")
        return

    u1, u2 = random.sample(users, 2)
    pair = random.choice(PAIRS)

    text = f"""
👑 {u1.mention_html()} ✨ {u2.mention_html()} 👑

🔥 Pair: {pair}

💌 Shayari:
"Yeh jodi nahi asaan,
Rab ne banayi hai khaas pehchaan 💖"
"""

    await update.message.reply_text(text, parse_mode="HTML")

# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("truth", truth))
    app.add_handler(CommandHandler("dare", dare))
    app.add_handler(CommandHandler("relation", relation))
    app.add_handler(CommandHandler("pair", pair))

    print("Bot running...")
    app.run_polling()