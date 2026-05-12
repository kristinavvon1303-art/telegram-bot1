import telebot
import time

TOKEN = "8464604971:AAEV5Y5wwX-uS5Fpw2iHTRHQe_GGl7xBN1k"
ADMINS = [5685078094]

bot = telebot.TeleBot(TOKEN)

waiting_users = {}

def typing(chat_id, text, delay=2):
    bot.send_chat_action(chat_id, 'typing')
    time.sleep(delay)
    bot.send_message(chat_id, text)


@bot.message_handler(commands=['asknereya'])
def ask_start(message):
    typing(
        message.chat.id,
        "П-привет!! Тебе надо что-то спросить у меня? Задавай, я отвечу на любой вопрос!"
    )
    waiting_users[message.chat.id] = True


@bot.message_handler(commands=['askchannel'])
def channel(message):
    typing(
        message.chat.id,
        (
            "Из какого я канала? Дай-ка вспомнить... А, точно! Я из... Аэ.. подожди-ка... А, всё, я вспомнила!\n\n"
            "Я из @NereyasUnderwaterWorld !\n\n"
            "Наверное, этот канал был создан в честь меня, ведь я отлично выполняла свою работу. По крайней мере, я надеюсь на это…"
        ),
        3
    )


@bot.message_handler(commands=['asknereyaabouther'])
def about(message):
    typing(
        message.chat.id,
        (
            "Хочешь узнать обо мне побольше? Тогда давай поговорим сначала о моих друзьях! \n\n"

            "Моя лучшая подруга это Джи джи, она часто подшучивает надо мной и говорит то, что медузы вкусные, хоть я и не особо понимаю о чём она. \n\n"

            "А ещё Браша, с ней весело проводить время и Кокоа, она мне часто помогает и выручает. Очень ценю их!\n\n"

            "Насчёт тунов, с которыми у меня не самые лучшие отношения.. Мне кажется, что Тиша меня слегка не долюбливает, ведь с меня постоянно падают капельки воды, которые ей режут глаза. \n\n"

            "А насчёт Финна… Один раз пока я спокойно шла к себе в комнату, он резко вышел из угла и кинул в меня рыбу! Я тогда так испугалась… С того момента я к нему больше не подхожу•••\n\n"

            "Мой MBTI это INFP. По крайней мере мне так сказала моя хозяйка.\n\n"

            "К сожалению я не помню кем были мои родители и я не знаю почему. Также я не очень помню своё прошлое…\n\n"

            "А, забыла сказать, что я плохо понимаю всякие намёки, а особенно какие-то романтические.\n\n"

            "Интересный факт! В моей комнате есть грубо говоря что-то наподобие потопа, так как на полу есть вода. Мне так комфортней, но я строго запрещаю Ви и другим электронным вещам приближаться к моей комнате."
        ),
        4
    )


@bot.message_handler(func=lambda message: message.chat.id in waiting_users)
def get_question(message):
    user_id = message.chat.id

    if message.text.startswith("/"):
        return

    for admin in ADMINS:
        bot.send_message(
            admin,
            f"ID: {user_id}\nВопрос:\n{message.text}"
        )

    del waiting_users[user_id]


@bot.message_handler(func=lambda message: message.chat.id in ADMINS)
def reply(message):
    if message.reply_to_message:
        try:
            user_id = int(
                message.reply_to_message.text.split("\n")[0].replace("ID: ", "")
            )
            typing(user_id, message.text, 2)
        except:
            pass


@bot.message_handler(func=lambda message: True)
def fallback(message):
    if message.chat.id not in ADMINS:
        typing(message.chat.id, "Используй /asknereya чтобы разбудить меня! (автоответчик)", 1.5)


bot.infinity_polling()

import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_web).start()
