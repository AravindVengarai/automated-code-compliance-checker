import requests
import os
from dotenv import load_dotenv

load_dotenv()

GREPTILE_API_KEY = os.getenv('GREPTILE_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
BASE_URL = 'https://api.greptile.com/v2/'

def submit_repo_for_indexing(remote, repository, branch):
    url = f'{BASE_URL}repositories'
    headers = {
        'Authorization': f'Bearer {GREPTILE_API_KEY}',
        'X-Github-Token': GITHUB_TOKEN,
        'Content-Type': 'application/json'
    }
    payload = {
        "remote": remote,
        "repository": repository,
        "branch": branch
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def check_indexing_status(repository_id):
    url = f'{BASE_URL}repositories/{repository_id}'
    headers = {
        'Authorization': f'Bearer {GREPTILE_API_KEY}',
        'X-Github-Token': GITHUB_TOKEN
    }
    response = requests.get(url, headers=headers)
    return response.json()

def query_codebase(question, repository_id):
    url = f'{BASE_URL}query'
    headers = {
        'Authorization': f'Bearer {GREPTILE_API_KEY}',
        'X-Github-Token': GITHUB_TOKEN,
        'Content-Type': 'application/json'
    }
    payload = {
        "messages": [
            {
                "id": "1",
                "content": question,
                "role": "user"
            }
        ],
        "repositories": [
            {
                "remote": "github",
                "repository": repository_id.split(':')[2],
                "branch": repository_id.split(':')[1]
            }
        ],
        "sessionId": "test-session-id"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
