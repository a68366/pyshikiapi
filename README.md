# pyshikiapi
Python wrapper for shikimori API

# Install
`pip install pyshikiapi`

# Usage
```
from pyshikiapi import API

app_name = 'YOUR_APP_NAME'
client_id = 'YOUR_APP_CLIENT_ID'
client_secret = 'YOUR_APP_SECRET'

api = API(app_name, client_id, client_secret)
print('Please visit the link and copy authorization code:', api.authorization_url)
code = input('The code: ')
api.fetch_token(code)

# Now you can use the api object to send requests
```

If you want to save the token to use it later, pass the `token_update_callback` argument to API:
```
def token_file_saver(token):  # A function which accepts 1 dict-like argument
    with open('token.json', 'w') as f:
        json.dump(token, f)

api = API(app_name, client_id, client_secret, token_update_callback=token_file_saver)
```

Next time you start, load the token:
```
with open('token.json') as f:
    token = json.load(f)
api = API(app_name, client_id, client_secret, token)
```

# Examples
```
api.animes.GET(page=2, limit=10)  # will send GET-request animes?page=2&limit=10
api.animes(5).roles.GET()  # will send GET-request animes/5/roles

comment = {'body': 'hello', 'commentable_type': 'User', 'commentable_id': 4193}
api.comments.POST(comment=comment, broadcast=False)
```
