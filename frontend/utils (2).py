import requests

BASE_URL = "http://localhost:8000"

def upload_function(name, language, timeout, code):
    payload = {
        "name": name,
        "language": language,
        "timeout": timeout,
        "code": code
    }
    res = requests.post(f"{BASE_URL}/functions/", json=payload)
    print("upload_function response:", res.status_code, res.text)
    return res.json()

def get_functions():
    res = requests.get(f"{BASE_URL}/functions/")
    print("get_functions response:", res.status_code, res.text)
    return res.json()

def run_function(function_id, use_gvisor=False):
    data = {"use_gvisor": str(use_gvisor).lower()}
    res = requests.post(f"{BASE_URL}/functions/{function_id}/run", data=data)
    print("run_function response:", res.status_code, res.text)
    return res.json()

def delete_function(function_id):
    res = requests.delete(f"{BASE_URL}/functions/{function_id}")
    print("delete_function response:", res.status_code, res.text)
    return res.json()

def get_logs(function_id):
    res = requests.get(f"{BASE_URL}/functions/{function_id}/logs")
    print("get_logs response:", res.status_code, res.text)
    return res.json()

def get_metrics(function_id):
    res = requests.get(f"{BASE_URL}/functions/{function_id}/metrics")
    print("get_metrics response:", res.status_code, res.text)
    return res.json()

def get_code(function_id):
    res = requests.get(f"{BASE_URL}/functions/{function_id}/code")
    print("get_code response:", res.status_code, res.text)
    return res.json()

def update_code(function_id, new_code):
    print(f"Updating Function {function_id} with code: {new_code[:100]}")
    res = requests.put(f"{BASE_URL}/functions/{function_id}", json={"code": new_code})
    print("update_code response:", res.status_code, res.text)
    return res.json()
