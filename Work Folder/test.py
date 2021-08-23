import requests


r = requests.get("https://v2.jokeapi.dev/joke/Any")
c = r.json()

print(c)
print( c['category'] )
print( c['type'] )
print( c['joke'] )
print( c['flags']['nsfw'] )
print( c['flags']['religious'] )
print( c['flags']['political'] )
print( c['flags']['racist'] )
print( c['flags']['sexist'] )
print( c['flags']['explicit'] )
print( c['lang'] )

