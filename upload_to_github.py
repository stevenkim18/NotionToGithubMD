import requests
import os

from dotenv import load_dotenv
from get_date import get_date
from exit import exit_program
from animated_loader import Loader

load_dotenv()

github_username = os.environ.get('GITHUB_USER_NAME')
github_repo_name = os.environ.get('GITHUB_REPO_NAME')
github_branch_name = os.environ.get('GITHUB_BRANCH')
folder_name = get_date()
md_filename = f"{get_date()}.md"

githubAPIURL = f"https://api.github.com/repos/{github_username}/{github_repo_name}/contents/{folder_name}/"

def upload_to_github(encode_data, filename):
    headers = {
        "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}",
        "Content-type": "application/vnd.github+json",
    }
    data = {
        "message": f"{get_date()} TIL", 
        "content": encode_data.decode('utf-8'),
        "branch": f"{github_branch_name}"
    }

    url = githubAPIURL
    url += filename

    loader = Loader('github에 업로드 중...')
    loader.start()

    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code in range(200, 299):
        loader.stop(f"🆗 '{filename}' 업로드 성공!")
    else:
        message = response.json()["message"]
        # 이미 파일명이 존재하면 sha 를 api에 같이 보내야 합니다.
        # sha는 github api에서 조회 가능합니다.
        if message == 'Invalid request.\n\n"sha" wasn\'t supplied.':
            print("이미 존재하는 파일 이름입니다!!")
        # 401 Bad Credentials -> github 토큰 만료. 
        print(f"상태 코드 : {response.status_code}")
        print(f"메시지 : {response.json()}")
        loader.stop(f"❌ '{filename}' 업로드 실패!")
        exit_program()

    