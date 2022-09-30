import requests
import time
import json
import telebot
import config
import bot_api

headers = {"user agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chro"
                         "me/102.0.0.0 Safari/537.36"}
url = "https://yobit.net/api/3/info"
API = bot_api.api_bot
bot = telebot.TeleBot(API)
purse = 100


def all_info_url():
    response = requests.get("https://yobit.net/api/3/info", headers=headers)
    with open("info.txt", "w") as file:
        file.write(response.text)


def main():
    print("Bot connect")
    all_info_url()


if __name__ == '__main__':
    main()
    bot.polling(none_stop=True)