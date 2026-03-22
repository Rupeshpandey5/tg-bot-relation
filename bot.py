import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from flask import Flask
from threading import Thread

BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

# -------- USER STORAGE -------- #
users = set()

def save_user(update: Update):
    user = update.effective_user
    if user and not user.is_bot:
        users.add((user.id, user.first_name))

# -------- DATA -------- #
TRUTHS = [
    "Sabse bada secret kya hai? 🤫",
    "Group me sabse zyada kaun pasand hai? 😏",
    "Kabhi kisi pe secret crush raha hai? 💘",
    "Pehli baar pyaar kab hua tha? 💕",
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

DARES = [
    "Apna nickname batao 😎",
    "Group me 3 emojis bhejo 🔥😂💯",
    "Apni current feeling ek emoji me batao 😊",
    "Kisi ek member ko tag karke hi bolo 👋",
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

RELATIONS = ["🤝 Besties","🖤 Toxic & Loyal","😈 Devil & Angel","👑 King & Queen",
"🐍 Snake & Charmer","⚡ Thunder & Lightning","😎 Boss & Queen","🤪 Drama Duo",
"🔥 Fire & Spark","🐒 Monkey & Banana","🍕 Pizza & Coke","🎧 DJ & Listener",
"💕 Love Birds","💖 Soulmates","💘 Heartbeat Duo","💞 Forever Pair",
"🌹 Rose & Thorn","🌙 Moon & Star","☀️ Sun & Shine","💫 Dream Pair",
"💎 Precious Bond","🌈 Rainbow Pair","💋 Kiss Couple","🎯 Perfect Match",
"🫶 Forever Together","🔥 Hot Couple","😎 Stylish Duo","🥰 Made For Each Other",
"💌 Hidden Love","💝 Special Connection","👀 Secret Lovers","💓 Heart Pair",
"💞 Love Connection","✨ Golden Pair","🌙 Night Couple","☀️ Sunshine Duo",
"🖤 Dark Love","💫 Star Couple","🔥 Fire Duo","💖 Dream Couple",
 "💕 Love Birds", "💖 Soulmates", "💘 Heartbeat Duo",
 "💞 Forever Pair", "🌙 Moon & Star", "🔥 Fire & Spark"
]

PAIR_NAMES = [
"👫 Dynamic Duo","💑 Sweethearts","🌈 Rainbow Friends","🎯 Perfect Pair",
"💥 Power Couple","🍀 Lucky Pair","🎵 Harmony Duo","⚡ Electric Pair",
"🌸 Blossom Buddies","🔥 Fire Pair","💘 Crush Couple","✨ Golden Duo",
"👑 Royal Pair","💞 Dil & Dhadkan","🫶 Bestie Pair","🤝 Best Duo",
"🖤 Toxic Duo","😈 Crazy Pair","💫 Star Pair","💎 Diamond Pair",
"💋 Kiss Duo","😍 Cute Pair","🥰 Lovely Couple","🎧 Music Pair",
"🍫 Sweet Duo","⚡ Energy Pair","👀 Secret Pair","💝 Special Duo",
"💌 Love Duo","👑 King Duo","🌈 Colorful Pair","💥 Blast Pair",
"🔥 Power Duo","💖 Dream Couple","😎 Cool Duo","💞 True Bond",
"✨ Perfect Match","🌙 Night Duo","☀️ Sunshine Pair","🎯 Exact Match",
"💘 Crush Couple", "✨ Golden Duo", "👑 King & Queen",
"💞 Dil & Dhadkan"

]

# -------- COMMANDS -------- #
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /truth, /dare, /relation or /pair")

async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    save_user(update)
    await update.message.reply_text(random.choice(TRUTHS))

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    save_user(update)
    await update.message.reply_text(random.choice(DARES))

# -------- RANDOM PAIR FROM USERS -------- #
def get_random_pair():
    if len(users) < 2:
        return None
    return random.sample(list(users), 2)

# -------- RELATION (GROUP ONLY) -------- #
async def relation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == "private":
        await update.message.reply_text("❌ Ye command sirf group me kaam karega!")
        return

    save_user(update)
    pair = get_random_pair()

    if not pair:
        await update.message.reply_text("😅 Members kam hai!")
        return

    u1, u2 = pair
    rel = random.choice(RELATIONS)

    msg = f"""
💘 𝙇𝙊𝙑𝙀 𝙍𝙀𝙇𝘼𝙏𝙄𝙊𝙉 💘

👤 <a href="tg://user?id={u1[0]}">{u1[1]}</a>
❤️
👤 <a href="tg://user?id={u2[0]}">{u2[1]}</a>

✨ {rel} ✨

🌹 Rab ne kuch khaas banaya hai 🌹  
💫 Dono ko ek saath milaya hai 💫  
💞 Shayad ye kismat ka ishara hai 💞  
😍 Inka connection sabse pyaara hai 😍
"""

    await update.message.reply_html(msg)

# -------- ADMIN PAIR -------- #
async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == "private":
        await update.message.reply_text("❌ Ye command sirf group me kaam karega!")
        return

    try:
        admins = await context.bot.get_chat_administrators(update.effective_chat.id)
        admin_ids = [a.user for a in admins if not a.user.is_bot]

        if len(admin_ids) < 2:
            await update.message.reply_text("😅 Admin kam hai!")
            return

        a1, a2 = random.sample(admin_ids, 2)
        pair_name = random.choice(PAIR_NAMES)

        msg = f"""
👑 𝘼𝘿𝙈𝙄𝙉 𝙋𝘼𝙄𝙍 👑

🔥 {a1.mention_html()}
💖
🔥 {a2.mention_html()}

✨ {pair_name} ✨

🌸 Dil se dil ka rishta bana 🌸  
💫 Ye koi simple baat nahi 💫  
❤️ Inki jodi sabse alag hai ❤️  
🥰 Dekhte hi pyaar ho jaye 🥰
"""

        await update.message.reply_html(msg)

    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

# -------- MESSAGE HANDLER (IMPORTANT) -------- #
async def track_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    save_user(update)

# -------- FLASK -------- #
app = Flask(__name__)

@app.route("/")
def index():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=PORT)

# -------- RUN BOT -------- #
def run_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("truth", truth))
    application.add_handler(CommandHandler("dare", dare))
    application.add_handler(CommandHandler("relation", relation))
    application.add_handler(CommandHandler("pair", pair))

    # track ALL messages
    application.add_handler(MessageHandler(filters.ALL, track_users))

    application.run_polling()

if __name__ == "__main__":
    Thread(target=run_flask).start()
    run_bot()