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


def fetch_pokemon_detail_by_name(name):
    response = requests.get(URL+f"/{name}")
    response.raise_for_status()
    return response.json()


def fetch_products_parallel(ids):
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(executor.map(fetch_pokemon_detail_by_id, ids))



if __name__ == "__main__":
    print("Este código execútase cando o script é executado directamente.")

    data = fetch_products_parallel([1,2])
    # data=fetch_all_pokemon(0, 10000000)
    
    print(data)
