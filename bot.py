import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ---------------- TRUTH & DARE QUESTIONS ---------------- #
TRUTH_QUESTIONS = [
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

DARE_QUESTIONS = [
    "Dance karke dikhao bina music ke!",
    "Apne phone ka last selfie share karo!",
    "Ek random emoji se poora sentence type karo!",
    "Apne piche ek funny face photo bhejo!",
    "Apne favorite song par 10 seconds gaao!",
    "Apne kisi dost ko random message bhejo 'I love you'.",
    "5 push-ups kar ke dikhao aur photo bhejo!",
    "Apne haath se ek funny drawing banao aur share karo!",
    "Apne browser history me sabse weird search dikhao!",
    "Apne favorite snack ka photo bhejo!",
    "Ek random line likho aur sabko chat me bhejo!",
    "Apne room ka sabse messy corner ka photo bhejo!",
    "Ek funny face banakar selfie bhejo!",
    "Apne pet ka photo share karo agar hai toh!",
    "Apne haath se ek short poem likho aur bhejo!",
    "Apne favorite movie ka dialogue act karo aur record share karo!",
    "Apne phone ka last video ka 5 sec clip share karo!",
    "Ek random dance move 10 sec ke liye karo aur photo/video bhejo!",
    "Apne shoes ka close-up photo bhejo!",
    "Kisi random object par funny caption likho aur share karo!"
]

# ---------------- RELATION & PAIR OPTIONS ---------------- #
RELATIONS = [
    "🤝 Besties", "🖤 Toxic & Loyal", "😈 Devil & Angel",
    "👑 King & Killer Queen", "🐍 Snake & Charmer", "⚡ Thunder & Lightning",
    "😎 Boss & Queen", "🤪 Drama King & Queen", "🔥 Fire & Spark",
    "🐒 Monkey & Banana", "🍕 Pizza & Coke", "🎧 DJ & Listener",
    "💕 Love Birds", "💖 Soulmates", "💘 Heartbeat Duo",
    "💞 Forever Pair", "🌹 Rose & Thorn", "🌙 Moon & Star",
    "☀️ Sun & Sunshine", "Best Friends Forever 🤝"
]

PAIRS = [
    "👫 Dynamic Duo", "💑 Sweethearts", "🌈 Rainbow Friends",
    "🎯 Perfect Pair", "💥 Power Couple", "🍀 Lucky Pair",
    "🎵 Harmony Duo", "⚡ Electric Pair", "🌸 Blossom Buddies",
    "🔥 Fire Pair" "🔥 Fire & Spark", "🌙 Moon & Star", "😎 Boss & Queen",
    "💘 Crush Couple", "✨ Golden Duo", "👑 King & Queen",
    "💞 Dil & Dhadkan", "🫶 Bestie Pair", "🤝 Besties",
    "🖤 Toxic & Loyal", "😈 Devil & Angel", "👑 King & Killer Queen"
]

# ---------------- COMMAND HANDLERS ---------------- #
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Main aapka fun bot hoon. Use these commands:\n"
        "/truth - Get a truth question\n"
        "/dare - Get a dare\n"
        "/relation - Fun relation with shayari\n"
        "/pair - Fun pair message"
    )

async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = random.choice(TRUTH_QUESTIONS)
    await update.message.reply_text(f"🤫 Truth: {question}")

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dare_text = random.choice(DARE_QUESTIONS)
    await update.message.reply_text(f"🎯 Dare: {dare_text}")

async def relation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Use: /relation username1 username2")
        return

    user1, user2 = context.args[:2]
    chosen_relation = random.choice(RELATIONS)
    shayari_list = [
        f"{user1} {chosen_relation} {user2}\n✨ Dil se dil tak ka rishta hai yeh!",
        f"{user1} {chosen_relation} {user2}\n🌹 Har pal yaad rakhna, yeh yaari pyari hoti hai!",
        f"{user1} {chosen_relation} {user2}\n💫 Do dil mile, par ek saath kaafi hai!"
    ]
    shayari = random.choice(shayari_list)
    await update.message.reply_text(shayari)

async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Use: /pair username1 username2")
        return

    user1, user2 = context.args[:2]
    chosen_pair = random.choice(PAIRS)
    emojis = ["🌟", "💫", "✨", "💖", "💞"]
    chosen_emoji = random.choice(emojis)

    shayari_list = [
        f"{user1} {chosen_emoji} {user2} - {chosen_pair}\n🌸 Saath ho toh har pal special lagta hai!",
        f"{user1} {chosen_emoji} {user2} - {chosen_pair}\n🎵 Har yaari me melody hoti hai!",
        f"{user1} {chosen_emoji} {user2} - {chosen_pair}\n🔥 Energy dono me perfect match hai!"
    ]
    shayari = random.choice(shayari_list)
    await update.message.reply_text(shayari)

# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"  # Replace with your bot token
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("truth", truth))
    app.add_handler(CommandHandler("dare", dare))
    app.add_handler(CommandHandler("relation", relation))
    app.add_handler(CommandHandler("pair", pair))

    print("Bot is running...")
    app.run_polling()