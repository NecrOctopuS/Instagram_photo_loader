import os
from dotenv import load_dotenv
import fetch_hubble
import fetch_spacex
from instabot import Bot

def main():
    images_path = 'Images/'
    os.makedirs(images_path, exist_ok=True)
    fetch_spacex.fetch_spacex_last_launch(images_path)
    fetch_hubble.fetch_hubble_collections(images_path)
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
            os.remove(f'{images_path}{pic}')

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()



