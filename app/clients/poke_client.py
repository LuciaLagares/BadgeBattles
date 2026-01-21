import requests
from concurrent.futures import ThreadPoolExecutor


URL = "https://pokeapi.co/api/v2/pokemon"


def fetch_all_pokemon(offset, limit):
# def fetch_all_pokemon():
    params = {
        "offset": offset,
        "limit": limit
    }
    response = requests.get(URL, params=params)
    # response = requests.get(URL)
    response.raise_for_status()
    return response.json()


def fetch_pokemon_detail_by_id(id):
    response = requests.get(URL+f"/{id}")
    response.raise_for_status()
    return response.json()

def fetch_pokemon_detail_by_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_pokemon_detail_by_name(name):
    response = requests.get(URL+f"/{name}")
    response.raise_for_status()
    return response.json()


def fetch_pokemons_parallel(urls):
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(fetch_pokemon_detail_by_url, urls))



if __name__ == "__main__":
    print("Este código execútase cando o script é executado directamente.")

    data = fetch_pokemons_parallel(["https://pokeapi.co/api/v2/pokemon/1/","https://pokeapi.co/api/v2/pokemon/2/","https://pokeapi.co/api/v2/pokemon/3/"])
    # data=fetch_all_pokemon(0, 10000000)
    for d in data:
        print(d["name"])
