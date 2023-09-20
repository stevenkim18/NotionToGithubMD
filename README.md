# NotionToGithubMD
Write in Notion and Upload to Github Automatically

## Requirement

- Python3
- [notion2md](https://github.com/echo724/notion2md)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Preparation

- Github Token
- Notion API Token

## How to use

1. Prepare all you need(Requirement, Tokens etc…)
2. Fill your `.env` file

```swift
GITHUB_USER_NAME = 
GITHUB_REPO_NAME = 
GITHUB_TOKEN = 

OUTPUT_PATH = "./output/"
```

3. Save your notion token in your local terminal<br>
(Set your notion api integrations first and then get token → https://www.notion.so/my-integrations)

```bash
export NOTION_TOKEN="{your_notion_token}"
```

4. Set Notion page that you want upload<br>
(If you set your **Connections** in page that you want, then you don’t need to set in your child page, only set **Connections** once in parent page)
<img width="500" src="https://github.com/stevenkim18/NotionToGithubMD/assets/35272802/04c64d01-5e08-425f-a452-d620021eb8f2">

5. Write down in Notion! And copy Notion link

<img width="522" alt="2" src="https://github.com/stevenkim18/NotionToGithubMD/assets/35272802/65dd3463-fa5b-404d-9d68-9a510ea0f791">

6. Run `main.py`
```bash
python3 main.py https://www.notion.so/{username}/{page_id}
```

## Demo
![demo720p](https://github.com/stevenkim18/NotionToGithubMD/assets/35272802/d53ee9d8-ee60-4a09-8684-9f9e8ecd6f42)

