import requests
from PIL import Image

EXTENSION_FOR_INSTAGRAM = [
    'jpg',
]
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

def define_extension(url):
    return url.split('.')[-1]

def fetch_hubble_id_image(image_id, images_path):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url)
    media = response.json()
    image_link_best_quality = media['image_files'][-1]['file_url']
    print(image_link_best_quality)
    if define_extension(image_link_best_quality) in EXTENSION_FOR_INSTAGRAM:
        right_url = f"https://{image_link_best_quality.replace('//imgsrc.', '')}".replace('hvi/', '')
        download_image(right_url, f'{image_id}.{define_extension(image_link_best_quality)}', images_path)
        square_image(f'{images_path}/{image_id}.{define_extension(image_link_best_quality)}')

def fetch_hubble_collections(images_path, collection_name='spacecraft'):
    collection_url = f'http://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(collection_url)
    medias = response.json()
    for media in medias:
        fetch_hubble_id_image(media['id'], images_path)