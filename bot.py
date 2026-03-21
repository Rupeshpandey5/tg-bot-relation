import os
import random
from threading import Thread
from flask import Flask
from telebot import TeleBot, types

# ---------------- BOT TOKEN ---------------- #
TOKEN = os.getenv("BOT_TOKEN")
bot = TeleBot(TOKEN)

# ---------------- FLASK APP ---------------- #
app = Flask(__name__)

# ---------------- DATA ---------------- #
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
    "Apni favourite food ka naam likho 🍕",
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

# ---------------- BOT COMMANDS ---------------- #
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hey! Main aapka Truth & Dare Bot hoon. 🎉\nCommands: /truth, /dare, /relation, /pair, /all")

@bot.message_handler(commands=["truth"])
def truth(message):
    bot.reply_to(message, f"💡 Truth: {random.choice(TRUTHS)}")

@bot.message_handler(commands=["dare"])
def dare(message):
    bot.reply_to(message, f"💪 Dare: {random.choice(DARES)}")

@bot.message_handler(commands=["relation"])
def relation(message):
    chat = message.chat
    if chat.type in ["group", "supergroup"]:
        try:
            members = bot.get_chat_administrators(chat.id)
            if len(members) < 2:
                bot.reply_to(message, "Group me kam se kam 2 admins hone chahiye.")
                return
            member1 = random.choice(members).user.first_name
            member2 = random.choice([m.user.first_name for m in members if m.user.first_name != member1])
            relation = random.choice(RELATIONS)
            bot.reply_to(message, f"{member1} ❤️ {member2} = {relation}")
        except:
            bot.reply_to(message, "Error fetching members. Ensure bot is admin.")
    else:
        bot.reply_to(message, "Ye command group me hi kaam karega.")

@bot.message_handler(commands=["pair"])
def pair(message):
    chat = message.chat
    if chat.type in ["group", "supergroup"]:
        admin_name = message.from_user.first_name
        pair_name = random.choice(PAIR_NAMES)
        bot.reply_to(message, f"{admin_name} ke liye pair: {pair_name}")
    else:
        bot.reply_to(message, "Ye command group me hi kaam karega.")

@bot.message_handler(commands=["all"])
def all_items(message):
    text = "💡 Truths:\n" + "\n".join(TRUTHS) + "\n\n💪 Dares:\n" + "\n".join(DARES)
    bot.reply_to(message, text)

# ---------------- START BOT IN THREAD ---------------- #
def start_bot():
    bot.infinity_polling()

Thread(target=start_bot).start()

# ---------------- FLASK ROUTE FOR RENDER PORT ---------------- #
@app.route("/")
def home():
    return "Bot is running ✅"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)