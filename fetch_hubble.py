import requests
from PIL import Image
import os

EXTENSION_FOR_INSTAGRAM = [
    '.jpg',
]
RECOMMENDED_PICTURE_SIZE_FOR_INSTAGRAM = 1080

def download_image(image_url, image_name, images_path):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(f'{images_path}/{image_name}', 'wb') as file:
        file.write(response.content)

def square_image(image_name):
    image = Image.open(image_name)
    if image.width == image.height:
        pass
    elif image.width > image.height:
        coordinates = ((image.width - image.height)/2, 0, image.width - (image.width - image.height)/2, image.height)
        image = image.crop(coordinates)
    else:
        coordinates = (0, (image.height - image.width)/2, image.width, image.height - (image.height - image.width)/2)
        image = image.crop(coordinates)
    if image.width > RECOMMENDED_PICTURE_SIZE_FOR_INSTAGRAM:
        image.thumbnail((RECOMMENDED_PICTURE_SIZE_FOR_INSTAGRAM, RECOMMENDED_PICTURE_SIZE_FOR_INSTAGRAM))
    image.save(image_name)

def fetch_hubble_id_image(image_id, images_path):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url)
    response.raise_for_status()
    media = response.json()
    image_link_best_quality = media['image_files'][-1]['file_url']
    if os.path.splitext(image_link_best_quality)[-1] in EXTENSION_FOR_INSTAGRAM:
        right_url = f"https://{image_link_best_quality.replace('//imgsrc.', '')}".replace('hvi/', '')
        download_image(right_url, f'{image_id}{os.path.splitext(image_link_best_quality)[-1]}', images_path)
        square_image(f'{images_path}/{image_id}{os.path.splitext(image_link_best_quality)[-1]}')

def fetch_hubble_collections(images_path, collection_name='spacecraft'):
    collection_url = f'http://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(collection_url)
    response.raise_for_status()
    medias = response.json()
    for media in medias:
        fetch_hubble_id_image(media['id'], images_path)