Python Username Enumeration & Password Brute Force Script

A simple script to perform username enumeration and password brute force attacks on web applications with login forms, using response length and HTTP status code analysis.
Designed for pentesting practice and automation learning in security labs like PortSwigger.
Features

* Username enumeration based on HTTP response length
* Password brute force based on HTTP status code and response length
* Reads username and password lists from files (usernames.txt and passwords.txt)
* Outputs valid usernames and successful logins to the console

Requirements

   Python 3.x
   requests library (install with pip install requests)

Usage
    Clone this repository:

git clone https://github.com/handvi/login-enum.git
cd login-enum

Prepare your wordlists:

* usernames.txt — list of usernames to test, one per line
* passwords.txt — list of passwords for brute force, one per line

Edit the target URL in the script (URL = "https://target.com/login") to your target.

Run the script:

    python login-enum.py

Disclaimer

This script is intended for educational purposes and authorized penetration testing only.
Do not use it for illegal activities or without explicit permission from the system owner.
License

MIT License — free to use and modify with attribution.
