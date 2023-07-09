
import requests
from dotenv import dotenv_values
from PIL import Image
from io import BytesIO

secrets = dotenv_values(".secrets")
API_URL = secrets['STABLE_DIFF_ENDPOINT']
headers = {"Authorization": f"Bearer {secrets['HUGGING_FACE_TOKEN']}"}

def query_image(input):
    payload = {"inputs": input}
    response = requests.post(API_URL, headers=headers, json=payload)
    image_bytes = response.content
    image = Image.open(BytesIO(image_bytes))
    return image