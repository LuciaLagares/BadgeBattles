import requests
from concurrent.futures import ThreadPoolExecutor
URL = "https://pokeapi.co/api/v2/pokemon"
URL_movements = "https://pokeapi.co/api/v2/move"
class PokeClient:
    def __init__(self):
        self._cache_pokemon = {}
        self._cache_moves_per_pokemon = {}
        self._cache_moves_data = {}

    def fetch_all_pokemons(self,url):
       response = requests.get(url)
       response.raise_for_status()
       return response.json()


    def fetch_pokemons(self,offset, limit):
       # def fetch_all_pokemon():
       params = {
           "offset": offset,
           "limit": limit
       }
       response = requests.get(URL, params=params)
       # response = requests.get(URL)
       response.raise_for_status()
       return response.json()


# def fetch_pokemon_detail_by_id(id):
#     response = requests.get(URL+f"/{id}")
#     response.raise_for_status()
#     return response.json()

    def fetch_pokemon_detail_by_id(self, id):
        if id in self._cache_pokemon:
            return self._cache_pokemon[id]
        response = requests.get(URL+f"/{id}")
        response.raise_for_status()
        data = response.json()
        self._cache_pokemon[id] = data
        return data

    def fetch_pokemon_detail_by_url(self,url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()


    def fetch_pokemon_detail_by_name(self,name):
        response = requests.get(URL+f"/{name}")
        response.raise_for_status()
        return response.json()


    def fetch_pokemons_parallel(self,ids):
        with ThreadPoolExecutor(max_workers=4) as executor:
            return list(executor.map(self.fetch_pokemon_detail_by_id,ids))
    
    def fetch_pokemons_moves_by_pokemon_id(self,id):
        if id in self._cache_moves_per_pokemon :
            return self._cache_moves_per_pokemon [id]
        raw_pokemon = self.fetch_pokemon_detail_by_id(id)
        data=raw_pokemon['moves']
        self._cache_moves_per_pokemon[id]=data
        return data


    def fetch_move_by_url(self,url_move):
        if url_move in self._cache_moves_data :
            return self._cache_moves_data [url_move]
        response = requests.get(url_move)
        response.raise_for_status()

        data=response.json()
        
        self._cache_moves_data[url_move]=data
        return data

poke_client = PokeClient()

    # def fetch_pokemons_moves_by_pokemon_id(id):
    #     raw_pokemon = fetch_pokemon_detail_by_id(id)
    #     return raw_pokemon['moves']


    # def fetch_move_by_url(url_move):

    #     response = requests.get(url_move)
    #     response.raise_for_status()

    #     return response.json()


if __name__ == "__main__":
    print("Este código execútase cando o script é executado directamente.")

    # data = fetch_pokemons_parallel(["https://pokeapi.co/api/v2/pokemon/1/","https://pokeapi.co/api/v2/pokemon/2/","https://pokeapi.co/api/v2/pokemon/3/"])
    # data=fetch_all_pokemon(0, 10000000)
    # for d in data:
    #     print(d["name"])








