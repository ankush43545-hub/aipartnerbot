import os
import telebot
import google.generativeai as genai

# Load API keys
TELEGRAM_TOKEN = os.getenv(8485580732:AAH3kwM1qHNcyZi18SUQ3j-fLmYL9ErQwMM)
GEMINI_API_KEY = os.getenv(gen-lang-client-0643157655)

bot = telebot.TeleBot(TELEGRAM_TOKEN)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

@bot.message_handler(func=lambda m: True)
def chat(message):
    user_msg = message.text

    try:
        response = model.generate_content(user_msg)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Error: " + str(e))

bot.polling()
