import base64
import os

from dotenv import load_dotenv

load_dotenv()

image_file_extensions = ('.png', '.jpg', '.gif', '.jpeg', '.bmp')
output_path = os.environ.get('OUTPUT_PATH')

def get_image_list():
    files = os.listdir(output_path)
    # 이미지 확장자만 필터링
    image_files = list(filter(lambda str: str.endswith(image_file_extensions), files))
    return image_files

def encode_image(image_filename):
    with open(f"{output_path}/{image_filename}", 'rb') as f:
        print(f"🎨 이미지 '{image_filename}' 오픈!")
        image_data = f.read()
        encoded_data = base64.b64encode(image_data)
        return encoded_data
