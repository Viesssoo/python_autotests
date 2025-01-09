import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8c657ea9f62b3e423e417c93cfb48e47'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN }

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}



response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(" ")
print("1 запрос: Создание покемона")
print(response_create.text)

pokemon_id = response_create.json()['id']

body_rename = {
    "pokemon_id": pokemon_id,
    "name": "Пипидастр",
    "photo_id": 1
}

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename )
print(" ")
print("----------------------------------------------------------")
print("2 запрос: Изменение покемона")
print(response_rename.text)

body_pokeball = {
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball )
print(" ")
print("----------------------------------------------------------")
print("3 запрос: Добавление в покебол")
print(response_pokeball.text)
print(" ")
