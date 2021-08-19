import requests
import json

url = f"https://api.chucknorris.io/jokes/random"
r = requests.get(url).json()
joke = r['value']
thumb = r['icon_url']


print(thumb)
