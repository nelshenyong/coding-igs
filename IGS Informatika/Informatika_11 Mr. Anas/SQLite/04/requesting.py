import requests


def get_100_pokemon_names():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=100'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return [pokemon['name'] for pokemon in data['results']]

def get_pokemon_details(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'name': name, 'error': f'Status code {response.status_code}'}


if __name__ == '__main__':
    names = get_100_pokemon_names()
    all_details = []

    for name in names:
        detail = get_pokemon_details(name)
        all_details.append(detail)
        print(f"Fetched: {detail['name']}")

   
    for i, p in enumerate(all_details[:5], 1):
        print(f"{i}. {p['name'].title()} - Height: {p['height']} - Weight: {p['weight']}")
