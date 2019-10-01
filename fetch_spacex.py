import requests
from PIL import Image

RECOMMENDED_PICTURE_SIZE_FOR_INSTAGRAM = 1080

def download_image(image_url, image_name, images_path):
    response = requests.get(image_url)
    with open(f'{images_path}/{image_name}', 'wb') as file:
        file.write(response.content)

def square_image(image_name):
    image = Image.open(image_name)
    if image.width == image.height:
        return
    elif image.width > image.height:
        coordinates = ((image.width - image.height)/2, 0, image.width - (image.width - image.height)/2, image.height)
    else:
        coordinates = ((image.height - image.width)/2, 0, image.width, image.height - (image.height - image.width)/2)
    image = image.crop(coordinates)
    if image.width > RECOMMENDED_PICTURE_SIZE_FOR_INSTAGRAM:
        image.thumbnail((RECOMMENDED_PICTURE_SIZE_FOR_INSTAGRAM, RECOMMENDED_PICTURE_SIZE_FOR_INSTAGRAM))
    image.save(image_name)

def fetch_spacex_last_launch(images_path):
    response = requests.get('https://api.spacexdata.com/v3/launches/latest')
    media = response.json()
    images_links = media["links"]['flickr_images']
    for image_index, images_link in enumerate(images_links):
        download_image(images_link, f'spacex{image_index}.jpg', images_path)
        square_image(f'{images_path}/spacex{image_index}.jpg')