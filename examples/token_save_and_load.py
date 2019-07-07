# For the first time, pass the 'login' argument to fetch user token:
#   python token_save_and_load.py login
# Then you can use the script normally:
#   python token_save_and_load.py

import json
import sys

from pyshikiapi import API

APP_NAME = 'YOUR_APP_NAME'
CLIENT_ID = 'YOUR_APP_CLIENT_ID'
CLIENT_SECRET = 'YOUR_APP_SECRET'


def token_file_saver(token):  # A function which accepts 1 dict-like argument
    with open('token.json', 'w') as f:
        json.dump(token, f)


def token_file_loader(filename='token.json'):
    with open(filename) as f:
        token = json.load(f)
        return token


def login(api):
    print('Please visit the link and copy authorization code:', api.authorization_url)
    code = input('The code: ')
    api.fetch_token(code)


def main():
    if sys.argv[-1] == 'login':
        api = API(APP_NAME, CLIENT_ID, CLIENT_SECRET, token_update_callback=token_file_saver)
        login(api)
        return
    else:
        token = token_file_loader()
        api = API(APP_NAME, CLIENT_ID, CLIENT_SECRET, token=token, token_update_callback=token_file_saver)

    # do some stuff
    print(api.devices.GET())


if __name__ == '__main__':
    main()
