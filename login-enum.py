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

def check_password(password):
    