import requests
import json
import os
from dotenv import load_dotenv

# .envファイルのパスを指定して読み込む
load_dotenv('.env')

# 環境変数を利用する
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')


# ワークフローの実行
def run_workflow(inputs, response_mode, user):
    url = f"{BASE_URL}/workflows/run"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "inputs": inputs,
        "response_mode": response_mode,
        "user": user
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        if response_mode == "blocking":
            result = response.json()
            if "data" in result and "outputs" in result["data"] and "text" in result["data"]["outputs"]:
                return result["data"]["outputs"]["text"]
            else:
                print("Error: 'text' not found in the API response.")
        elif response_mode == "streaming":
            for chunk in response.iter_content(chunk_size=None):
                if chunk:
                    print(chunk.decode())
    else:
        print(f"Request failed with status code {response.status_code}")


# ワークフローの停止
def stop_workflow(task_id, user):
    url = f"{BASE_URL}/workflows/{task_id}/stop"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"user": user}
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")


# アプリケーション情報の取得
def get_parameters(user):
    url = f"{BASE_URL}/parameters?user={user}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")



