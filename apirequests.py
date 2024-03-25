# apirequests.py
import urequests


def task_data_get(api_url_param, api_key_param):
    headers = {
        "Authorization": api_key_param,
        "Content-Type": "application/json"
    }
    response = urequests.get(api_url_param, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch task data", response.status_code)
        return None


api_url = "https://api.monday.com/v2"
api_key = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjMzNzc0MjMyNCwiYWFpIjoxMSwidWlkIjoyMTM0MjAzMCwiaWFkIjoiMjAyNC0wMy0yNVQyMDozOTo1NC43MTlaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6ODY4MjEwNiwicmduIjoidXNlMSJ9.hT8cGjj5RdKYqI_BulaVmqh7413n8XV3HxYzkz-_kyM"
task_data = task_data_get(api_url, api_key)
print(task_data)
