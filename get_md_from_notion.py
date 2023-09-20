import base64
import os

from notion2md.exporter.block import MarkdownExporter
from exit import exit_program
from dotenv import load_dotenv
from animated_loader import Loader

load_dotenv()

output_path = os.environ.get('OUTPUT_PATH')
md_string = ''

def get_md_from_notion(url):
    loader = Loader('마크다운 가져오는 중...').start()
    try:
        MarkdownExporter(block_url=url,
                            output_path= output_path,
                            output_filename='post',
                            download=True, 
                            unzipped=True).export()
        loader.stop('🆗 마크다운 가져오기 성공!')
    except ValueError:
        loader.stop('⛔️ 유효하지 않은 Notion url 입니다. url을 다시 한 번 확인해주세요.')
        exit_program()
        

def get_encoded_md_data():
    with open(f"{output_path}post.md") as f:
        md_string = f.read()
    utf8_data = md_string.encode('utf-8')
    encode_data = base64.b64encode(utf8_data)
    return encode_data

