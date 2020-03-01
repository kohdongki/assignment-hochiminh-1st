import requests
import webbrowser

url = "https://api.instagram.com/oembed"

params = {'url': 'https://www.instagram.com/p/B8OBL7BDEpL/'}

req = requests.get(url, params=params)
print(req.url)

# res = req.json()['results']
# location = res[0]['title']
# print(location)

res = req.json()['title']
print(res)