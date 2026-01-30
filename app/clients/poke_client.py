import time
from typing import OrderedDict
import requests
from concurrent.futures import ThreadPoolExecutor
URL = "https://pokeapi.co/api/v2/pokemon"
URL_movements = "https://pokeapi.co/api/v2/move"


class PokeClient:
    def __init__(self):
        self._cache_pokemon = OrderedDict()
        self._cache_moves_per_pokemon = OrderedDict()
        self._cache_moves_data = OrderedDict()

    def fetch_all_pokemons(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except:
            return None

    def fetch_pokemons(self, offset, limit):
        try:
            params = {
                "offset": offset,
                "limit": limit
            }
            response = requests.get(URL, params=params)
            # response = requests.get(URL)
            response.raise_for_status()
            return response.json()

        except:
            return None


# def fetch_pokemon_detail_by_id(id):
#     response = requests.get(URL+f"/{id}")
#     response.raise_for_status()
#     return response.json()


    def fetch_pokemon_detail_by_id(self, id):
        now = time.time()
        TTL = now + 120
        size = 20
        try:
            if id in self._cache_pokemon:
                if now < self._cache_pokemon[id]["TTL_key"]:
                    data = self._cache_pokemon[id]["data_key"]
                    return data
            response = requests.get(URL+f"/{id}")
            response.raise_for_status()
            data = response.json()
            dataTTL = {"data_key": data,
                       "TTL_key": TTL}
            if len(self._cache_pokemon) >= size:
                self._cache_pokemon.popitem(last=True)
                self._cache_pokemon[id] = dataTTL
            else:
                self._cache_pokemon[id] = dataTTL

            return data

        except Exception as e:
            print("ERROR", e)
            return None

    def fetch_pokemon_detail_by_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except:
            return None

    def fetch_pokemon_detail_by_name(self, name):
        try:
            response = requests.get(URL+f"/{name}")
            response.raise_for_status()
            return response.json()
        except:
            return None

    def fetch_pokemons_parallel(self, ids):
        with ThreadPoolExecutor(max_workers=4) as executor:
            return list(executor.map(self.fetch_pokemon_detail_by_id, ids))

    def fetch_pokemons_moves_by_pokemon_id(self, id):
        now = time.time()
        TTL = now + 120
        size = 100
        try:
            if id in self._cache_moves_per_pokemon:
                if now < self._cache_moves_per_pokemon[id]["TTL_key"]:
                    data = self._cache_moves_per_pokemon[id]["data_key"]
                return data
            raw_pokemon = self.fetch_pokemon_detail_by_id(id)

            data = raw_pokemon['moves']
            dataTTL = {"data_key": data, "TTL_key": TTL}
            if len(self._cache_moves_per_pokemon) >= size:
                self._cache_pokemon.popitem(last=True)
                self._cache_moves_per_pokemon[id] = dataTTL
            else:
                self._cache_moves_per_pokemon[id] = dataTTL
            return data
        except:
            return None

    def fetch_move_by_url(self, url_move):
        now = time.time()
        TTL = now + 120
        size = 100
        try:
            if url_move in self._cache_moves_data:
                if now < self._cache_moves_data[url_move]["TTL_key"]:
                    data = self._cache_moves_data[url_move]["data_key"]
                return data
            response = requests.get(url_move)
            response.raise_for_status()
            data = response.json()
            dataTTL = {"data_key": data,
                       "TTL_key": TTL}
            if len(self._cache_moves_data) >= size:
                self._cache_moves_data.popitem(last=True)
                self._cache_moves_data[url_move] = dataTTL
            else:
                self._cache_moves_data[url_move] = dataTTL
            return data
        except:
            return None


poke_client = PokeClient()


if __name__ == "__main__":
    print("Este código execútase cando o script é executado directamente.")

    # def fetch_move_by_url(self, url_move):
    #     now = time.time()
    #     TTL = now + 120
    #     size = 100
    #     try:
    #         if url_move in self._cache_moves_data:
    #             if now < self._cache_moves_data[url_move]["TTL_key"]:
    #                 data = self._cache_moves_data[id]["data_key"]
    #             return data
    #         response = requests.get(url_move)
    #         response.raise_for_status()
    #         data = response.json()
    #         dataTTL = {"data_key": data,
    #                    "TTL_key": TTL}
    #         if len(self._cache_moves_data)>=size:
    #             self._cache_moves_data.popitem(last=True)
    #             self._cache_moves_data[url_move]= dataTTL
    #         else:
    #             self._cache_moves_data[url_move]= dataTTL
    #         return data
    #     except:
    #         return None

    # def fetch_move_by_url(self, url_move):
    #     try:
    #         if url_move in self._cache_moves_data:
    #             return self._cache_moves_data[url_move]
    #         response = requests.get(url_move)
    #         response.raise_for_status()
    #         data = response.json()
    #         self._cache_moves_data[url_move] = data
    #         return data
    #     except:
    #         return None

    # def fetch_pokemons_moves_by_pokemon_id(self, id):
    #     try:
    #         if id in self._cache_moves_per_pokemon:
    #             return self._cache_moves_per_pokemon[id]
    #         raw_pokemon = self.fetch_pokemon_detail_by_id(id)
    #         data = raw_pokemon['moves']
    #         self._cache_moves_per_pokemon[id] = data
    #         return data
    #     except:
    #         return None
