import os
import requests

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_BASE_PATH = os.path.join(CURRENT_DIR, "images")

os.makedirs(IMAGE_BASE_PATH, exist_ok=True)

def get_extention(image_url: str) -> str | None:
    extentions: list[str] = [".png", ".jpeg", ".jpg", ".svg"]

    for extention in extentions:
        if extention in image_url:
            return extention

def download_image(image_url: str, name: str, folder: str = None) -> None:
    if extension := get_extention(image_url):
        if folder:
            image_name: str = f"{folder}/{name}{extension}"
        else:
            image_name: str = f"{name}{extension}"
    else:
        raise Exception("Image extention could not be located.")

    if os.path.isfile(image_name):
        raise Exception(f"File name already exists.")

    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, "wb") as handler:
            handler.write(image_content)
            print(f"Downloaded: {image_name} successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_url: str = input("enter a url: ")
    input_name: str = input("enter a name: ")
    print("downloading...")

    download_image(input_url, name=input_name, folder=f"{IMAGE_BASE_PATH}")