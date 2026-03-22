import os
import random
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
PORT = int(os.environ.get("PORT", 10000))

app = Flask(__name__)
telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()

# ---------------- TRUTH (40) ---------------- #
TRUTHS = [
"Sabse bada secret kya hai? 🤫","Kisi pe crush hai? 😏","Last kis se chat ki thi? 📱","Pehla pyaar kab hua? 💕",
"Sabse embarrassing moment? 😳","Kabhi jhoot pakda gaya? 😅","Kisi ko propose kiya? 💘","Favorite person kaun hai? ❤️",
"Kabhi heartbreak hua? 💔","Apni love life describe karo 😆","Kisi se jalte ho? 😏","Kabhi kisi ko ignore kiya? 🙄",
"Kabhi roye ho kisi ke liye? 😢","Kisi ka phone check kiya? 📲","Kabhi cheat kiya exam me? 📚",
"Kisi ko secretly stalk karte ho? 👀","Sabse zyada kispe trust hai? 🤝","Kabhi kisi ko block kiya? 🚫",
"Kisi se abhi bhi pyaar hai? 💞","Apna biggest fear kya hai? 😨",
"Aapne sabse ajeeb sapna kab dekha?","Aapne apni life me sabse embarrassing moment kya tha?",
"Aapne kab kisi ko chupke se like kiya tha?","Aapka first crush kaun tha?",
"Aapne sabse bada jhoot kab bola?","Aapki koi aisi habit jo sabko irritate karti ho?",
"Aapne apni life me kab kisi ko hurt kiya?","Aapne kab kisi secret ko leak kiya?",
"Aapko sabse zyada jealousy kab mehsoos hui?","Aapka favorite childhood memory kya hai?",
"Aapne kab kisi ke liye kuch acha kiya bina wajah?","Aapki life me sabse crazy moment kya tha?",
"Aapne kab kisi ko silently admire kiya?","Aapne sabse weird food combination kab try kiya?",
"Aapka sabse bada fear kya hai?","Aapka favorite hobby kya hai?",
"Aapne kab kisi se sorry bola without meaning it?","Aapki hidden talent kya hai?",
"Aapne kab kisi ke saath overreact kiya?","Aapki dream destination kahaan hai?"
]

# ---------------- DARE (30) ---------------- #
DARES = [
"Dance karke dikhao bina music ke! 💃","Apne phone ka last selfie share karo! 📸",
"Ek random emoji se poora sentence type karo 😂","Funny face selfie bhejo 😜",
"10 sec gaana gao 🎤","Kisi ko 'I love you' msg bhejo ❤️",
"5 push-ups karo 💪","Funny drawing bhejo 🎨",
"Browser history ka weird search batao 😅","Favorite snack ka pic bhejo 🍕",
"Random line group me bhejo 🤣","Room ka messy corner dikhao 🏠",
"Funny selfie bhejo 😆","Pet ka photo share karo 🐶",
"Short poem likho ✍️","Movie dialogue act karo 🎬",
"Last video ka 5 sec clip bhejo 🎥","Dance move dikhao 🔥",
"Shoes ka close-up bhejo 👟","Random object pe caption likho 😂",
"3 emojis bhejo 😂🔥😎","Kisi ko compliment do 💐",
"Apni crush type batao 😏","Fav song batao 🎵",
"Kisi ko roast karo 😈","Funny line likho 🤣",
"Kisi ko best friend bolo 🤝","Apni pic bhejo 😜",
"Kisi ko 'I miss you' bolo 😢","Apni feeling emoji me batao 😊"
]

# ---------------- RELATION (40) ---------------- #
RELATIONS = [
"🤝 Besties","🖤 Toxic & Loyal","😈 Devil & Angel","👑 King & Queen",
"🐍 Snake & Charmer","⚡ Thunder & Lightning","😎 Boss & Queen","🤪 Drama Duo",
"🔥 Fire & Spark","🐒 Monkey & Banana","🍕 Pizza & Coke","🎧 DJ & Listener",
"💕 Love Birds","💖 Soulmates","💘 Heartbeat Duo","💞 Forever Pair",
"🌹 Rose & Thorn","🌙 Moon & Star","☀️ Sun & Shine","💫 Dream Pair",
"💎 Precious Bond","🌈 Rainbow Pair","💋 Kiss Couple","🎯 Perfect Match",
"🫶 Forever Together","🔥 Hot Couple","😎 Stylish Duo","🥰 Made For Each Other",
"💌 Hidden Love","💝 Special Connection","👀 Secret Lovers","💓 Heart Pair",
"💞 Love Connection","✨ Golden Pair","🌙 Night Couple","☀️ Sunshine Duo",
"🖤 Dark Love","💫 Star Couple","🔥 Fire Duo","💖 Dream Couple"
]

# ---------------- PAIR (40) ---------------- #
PAIRS = [
"👫 Dynamic Duo","💑 Sweethearts","🌈 Rainbow Friends","🎯 Perfect Pair",
"💥 Power Couple","🍀 Lucky Pair","🎵 Harmony Duo","⚡ Electric Pair",
"🌸 Blossom Buddies","🔥 Fire Pair","💘 Crush Couple","✨ Golden Duo",
"👑 Royal Pair","💞 Dil & Dhadkan","🫶 Bestie Pair","🤝 Best Duo",
"🖤 Toxic Duo","😈 Crazy Pair","💫 Star Pair","💎 Diamond Pair",
"💋 Kiss Duo","😍 Cute Pair","🥰 Lovely Couple","🎧 Music Pair",
"🍫 Sweet Duo","⚡ Energy Pair","👀 Secret Pair","💝 Special Duo",
"💌 Love Duo","👑 King Duo","🌈 Colorful Pair","💥 Blast Pair",
"🔥 Power Duo","💖 Dream Couple","😎 Cool Duo","💞 True Bond",
"✨ Perfect Match","🌙 Night Duo","☀️ Sunshine Pair","🎯 Exact Match"
]

# ---------------- SHAYARI ---------------- #
def shayari_line(u1, u2, rel):
    lines = [
        f"💖 {u1} ❤️ {u2}\n✨ {rel}\n💫 Rab ne likhi hai yeh kahani, dono ki jodi lage mastani!",
        f"🌸 {u1} 💞 {u2}\n🔥 {rel}\n💌 Dil se dil tak connection strong, saath rahe toh life hai long!",
        f"👑 {u1} 💖 {u2}\n💫 {rel}\n🌹 Yeh rishta nahi khel, dono ek dusre ke dil ka mail!",
        f"💓 {u1} 💘 {u2}\n✨ {rel}\n🔥 Jodi ho toh aisi ho, full vibe aur classy ho!"
    ]
    return random.choice(lines)

# ---------------- COMMANDS ---------------- #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bot Ready!\n\n/truth\n/dare\n/relation\n/pair")

async def truth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🤫 Truth:\n{random.choice(TRUTHS)}")

async def dare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🎯 Dare:\n{random.choice(DARES)}")

# 🔥 RELATION (random members)
async def relation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    members = await context.bot.get_chat_administrators(chat.id)
    users = [m.user for m in members if not m.user.is_bot]

    if len(users) < 2:
        return await update.message.reply_text("Members kam hai 😅")

    u1, u2 = random.sample(users, 2)

    name1 = u1.mention_html()
    name2 = u2.mention_html()

    rel = random.choice(RELATIONS)

    await update.message.reply_text(
        shayari_line(name1, name2, rel),
        parse_mode="HTML"
    )

# 🔥 PAIR (only admins)
async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    admins = await context.bot.get_chat_administrators(chat.id)
    users = [a.user for a in admins if not a.user.is_bot]

    if len(users) < 2:
        return await update.message.reply_text("Admins kam hai 😅")

    u1, u2 = random.sample(users, 2)

    name1 = u1.mention_html()
    name2 = u2.mention_html()

    pair = random.choice(PAIRS)

    await update.message.reply_text(
        shayari_line(name1, name2, pair),
        parse_mode="HTML"
    )

# ---------------- HANDLERS ---------------- #
telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("truth", truth))
telegram_app.add_handler(CommandHandler("dare", dare))
telegram_app.add_handler(CommandHandler("relation", relation))
telegram_app.add_handler(CommandHandler("pair", pair))

# ---------------- WEBHOOK ---------------- #
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    telegram_app.update_queue.put_nowait(update)
    return "ok"

@app.route("/")
def home():
    return "Bot Running ✅"

# ---------------- START ---------------- #
if __name__ == "__main__":
    telegram_app.bot.set_webhook(f"{WEBHOOK_URL}/{BOT_TOKEN}")
    app.run(host="0.0.0.0", port=PORT)