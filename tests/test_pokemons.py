import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8c657ea9f62b3e423e417c93cfb48e47'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '16453'

def test_response_status_code():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id': TRAINER_ID} )
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id': TRAINER_ID} )
    assert response.json()['data'][0]['trainer_name'] == 'Хуба Буба'