import os
from io import BytesIO

import requests
import telebot
from PIL import Image
from telebot import types

from backend import settings

bot = telebot.TeleBot('6442182992:AAFF7xkljKsaHEmNh0PfE9k2rMXjZbGii0s')
chat_id = '@My_Alpha_Doors'


def send_message_to_bot(message):
    try:
        bot.send_message(chat_id, message)
    except Exception as e:
        print(f"Произошла ошибка при отправке сообщения в Telegram: {str(e)}")


def send_photo_with_message_to_bot(link, message):
    try:
        print(f"{settings.BASE_DIR}{link}")
        photo_path = f"{settings.BASE_DIR}{link}"
        photo_input = types.InputFile(photo_path)
        bot.send_photo(chat_id, photo_input, caption=message)
    except Exception as e:
        print(f"Произошла ошибка при отправке сообщения в Telegram: {str(e)}")


if __name__ == "__main__":
    message = "This is a test message sent to the channel."
    send_message_to_bot(message)


def overlay_images(image_urls):
    images = [Image.open(BytesIO(requests.get(url).content)).convert("RGBA") for url in image_urls]

    base_image = images[0]

    for img in images[1:]:
        base_image = Image.alpha_composite(base_image, img)

    return base_image


def process_and_send_images(image_urls):
    final_image = overlay_images(image_urls)
    send_image_to_telegram(final_image)


def send_image_to_telegram(image):
    image_path = "result.png"
    image.save(image_path, "PNG")

    with open(image_path, "rb") as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)

    # Удаляем временный файл
    os.remove(image_path)
