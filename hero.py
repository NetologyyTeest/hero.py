import requests
url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
hero = response.json()
hero_name = []
hero_name.append(hero[106])
hero_name.append(hero[236])
hero_name.append(hero[506])
dict_hero = {}
for hero in hero_name:
    dict_hero[hero['name']] = hero['powerstats']['intelligence']
hero_sorted = {k: v for k, v in sorted(dict_hero.items(), key=lambda item: item[1], reverse=True)}
print(f'Самый умный супергерой {list(hero_sorted.keys())[0]}')
