import os
from dotenv import load_dotenv

load_dotenv()

output_path = os.environ.get('OUTPUT_PATH')

def delete_files_in_folder():
    # 폴더 안에 있는 파일 목록을 가져옵니다.
    file_list = os.listdir(output_path)

    # 파일을 하나씩 순회하며 삭제합니다.
    for file_name in file_list:
        file_path = os.path.join(output_path, file_name)
        try:
            # 파일이 디렉터리인지 확인하고 디렉터리인 경우 재귀적으로 삭제합니다.
            if os.path.isdir(file_path):
                delete_files_in_folder(file_path)
            else:
                os.remove(file_path)
                print(f"{file_path} 파일을 삭제했습니다.")
        except Exception as e:
            print(f"파일 삭제 중 오류 발생: {e}")
    