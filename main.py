from get_md_from_notion import get_md_from_notion
from get_md_from_notion import get_encoded_md_data
from upload_to_github import upload_to_github
from encode_image import get_image_list
from encode_image import encode_image
from get_date import get_date
from exit import exit_program

import sys

if len(sys.argv) < 2:
    print("⛔️ 노션 url를 main.py 뒤에 넣어주세요.")
    exit_program()
    

notion_url = sys.argv[1]

get_md_from_notion(notion_url)

md_data = get_encoded_md_data()
md_filename = f"{get_date()}.md"

# md 파일 업로드
upload_to_github(md_data, md_filename)

# 이미지들 업로드
for image_name in get_image_list():
    encoded_image_data = encode_image(image_name)
    upload_to_github(encoded_image_data, image_name)
