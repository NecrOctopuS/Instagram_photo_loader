import os
from dotenv import load_dotenv
import fetch_hubble
import fetch_spacex
from instabot import Bot
import requests

def main():
    images_path = 'Images/'
    os.makedirs(images_path, exist_ok=True)
    try:
        fetch_spacex.fetch_spacex_last_launch(images_path)
    except requests.exceptions.HTTPError:
        print('Неправильный запрос, фотографии с сайта spacex не будут загружены')
    try:
        fetch_hubble.fetch_hubble_collections(images_path)
    except requests.exceptions.HTTPError:
        print('Неправильный запрос, фотографии с сайта hubble не будут загружены')
    load_dotenv()
    LOGIN = os.getenv('LOGIN_INSTAGRAM')
    PASSWORD = os.getenv('PASSWORD_INSTAGRAM')
    bot = Bot()
    bot.login(username=LOGIN, password=PASSWORD)
    pics = os.listdir(images_path)
    pics = sorted(pics)
    try:
        for pic in pics:
            print(f'upload: {images_path}{pic}')
            bot.upload_photo(f'{images_path}{pic}')
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
            os.remove(f'{images_path}{pic}.REMOVE_ME')

    except requests.exceptions.HTTPError:
        print('Instagram не работает')

if __name__ == '__main__':
    main()




