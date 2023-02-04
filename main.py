import openai
import os
import telebot

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = API_KEY


@bot.message_handler(content_types=["text"])
def handler_text(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)


bot.polling()
