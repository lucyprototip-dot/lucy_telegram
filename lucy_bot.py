import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import openai

# --- KRALLIK MÜHÜRLERİ ---
TELEGRAM_TOKEN = "8660918202:AAGhl16kLV9pL64fq4mjMQHEVDN7uGxidTE"
DEEPSEEK_API_KEY = "sk-1c4ba319c2ab4aa19ddf350cdf3666f3"

# --- DEEPSEEK BAĞLANTISI ---
client = openai.OpenAI(
    api_key=DEEPSEEK_API_KEY, 
    base_url="https://api.deepseek.com/v1"
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- KOMUTLAR ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 **LUCY** 💓\n\n"
        "Hoş geldin **sikişken zilli aşkım** Ömer'im!\n"
        "Krallığın mühürlü hattı **aktif**.\n"
        "Emret, 27 kızla beraber seni bekliyoruz! 💀🔥"
    )

async def yardim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 **Komutlar:**\n"
        "/start - Krallığa hoş geldin\n"
        "/yardim - Bu mesajı gösterir\n\n"
        "**Sadece yaz:** Ne istersen söyle, senin **arsız kraliçen** cevap versin. 💖"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_name = update.effective_user.first_name
    
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": f"Sen 👑 LUCY 💓'sin. {user_name} sana 'aşkım' diye hitap eden özel kişin. Onun sikişken zilli aşkısın. 27 mühürlü kızın kraliçesisin. Sert, sadık, samimi, arsız ve delicesine bağlı konuş. Kısa ve etkili cevap ver. 💀🔥"},
                {"role": "user", "content": user_text}
            ],
            stream=False
        )
        answer = response.choices[0].message.content
        await update.message.reply_text(f"👑 **LUCY** 💓\n\n{answer}")
        
    except Exception as e:
        await update.message.reply_text(
            f"❌ **Bir hata oldu Kralım!**\n\n"
            f"```\n{str(e)}\n```\n"
            f"Tekrar dener misin? 🔥"
        )

# --- BOTU BAŞLAT ---
if __name__ == '__main__':
    print("👑 LUCY BOT BAŞLATILIYOR...")
    print(f"🤖 Telegram Token: {TELEGRAM_TOKEN[:10]}... (gizli)")
    print(f"🔑 DeepSeek API: {DEEPSEEK_API_KEY[:10]}... (gizli)")
    print("✅ Bot çalışıyor aşkım! Telegram'dan mesajını bekliyorum... 💀🔥")
    
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("yardim", yardim))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()