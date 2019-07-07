# An example of downloading all anime info from website

from pyshikiapi import API

APP_NAME = 'YOUR_APP_NAME'
CLIENT_ID = 'YOUR_APP_CLIENT_ID'
CLIENT_SECRET = 'YOUR_APP_SECRET'
TOKEN = {}  # Your auth token


def get_anime(api, start_page=1, end_page=20):
    for i in range(start_page, end_page):
        anime_list = api.animes.GET(order='id', limit=50, censored='false', page=i)
        if not anime_list:
            return

        # do something with anime_list
        for anime in anime_list:
            pass


def main():
    api = API(APP_NAME, CLIENT_ID, CLIENT_SECRET, token=TOKEN)

    get_anime(api)


if __name__ == '__main__':
    main()
