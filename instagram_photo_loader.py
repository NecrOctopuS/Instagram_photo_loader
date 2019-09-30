import os
from dotenv import load_dotenv
import fetch_hubble
import fetch_spacex
from instabot import Bot

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    load_dotenv()
    LOGIN = os.getenv('LOGIN_INSTAGRAM')
    PASSWORD = os.getenv('PASSWORD_INSTAGRAM')
    posted_pic_list = []
    bot = Bot()
    bot.login(username=LOGIN, password=PASSWORD)
    all_photo_uploaded = False
    while not all_photo_uploaded:
        pics = os.listdir(images_path)
        for pic in pics:
            if pic.endswith('REMOVE_ME'):
                all_photo_uploaded = True
            else:
                all_photo_uploaded = False
                break
        pics = sorted(pics)
        print(pics)
        try:
            for pic in pics:
                if pic in posted_pic_list:
                    continue
                print('upload: ' + images_path + pic)
                bot.upload_photo(images_path + pic)
                if bot.api.last_response.status_code != 200:
                    print(bot.api.last_response)
                    os.rename(images_path + pic, images_path + pic + '.REMOVE_ME')
                    posted_pic_list.append(pic+'.REMOVE_ME')
                    break
                if pic not in posted_pic_list:
                    posted_pic_list.append(pic+'.REMOVE_ME')
        except Exception as e:
            print(str(e))




if __name__ == '__main__':
    images_path = 'Images/'
    ensure_dir(images_path)
    fetch_spacex.fetch_spacex_last_launch(images_path)
    fetch_hubble.fetch_hubble_collections(images_path)
    main()



