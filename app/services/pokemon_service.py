from app.clients.adaptor import poke_adaptor
from app.clients.adaptor.poke_adaptor import from_api_move_to_move, from_api_to_pokemon, from_api_to_pokemon_list
import app.repositories.pokemon_repo as pokemon_repo
from app.clients.poke_client import poke_client
# import app.clients.poke_client as poke_client
import random
import math


# def get_pokemons():
#     return pokemon_repo.get_pokemons()

def get_pokemons():
    # Este busca todos los pokemons para poder elegir el pokemon rival aleatoriamente
    URL = "https://pokeapi.co/api/v2/pokemon?limit=1000000"
    # data = poke_client.fetch_all_pokemon(0,8)
    data = poke_client.fetch_all_pokemons(URL)
    if data is None:
        return None

    return data["results"]


def get_list_pokemons(offset, limit):
    # Para listar pokemons para elegir
    data = poke_client.fetch_pokemons(offset, limit)
    if data is None:

        return None
    list_pokemons = data["results"]

    if list_pokemons is None:

        return None, data["count"]
    ids = []
    for item_pokemon in list_pokemons:
        #       url="https://pokeapi.co/api/v2/pokemon/1/"
        # urls=url.split("/")
        # print("hola",urls[len(urls)-2])
        url = item_pokemon["url"]
        urls = url.split("/")
        id = urls[len(urls)-2]
        ids.append(id)

    raw_pokemons = poke_client.fetch_pokemons_parallel(ids)
    if raw_pokemons is None:

        return None, data["count"]

    pokemons_without_moves = from_api_to_pokemon_list(raw_pokemons)

    return pokemons_without_moves, data["count"]


def get_moves_from_api(pokemons):
    for pokemon in pokemons:
        get_moves_from_api_individual(pokemon)
    return pokemons


def get_moves_from_api_individual(pokemon):
    clean_moves = []
    raw_moves = poke_client.fetch_pokemons_moves_by_pokemon_id(pokemon.id)
    cnt = len(raw_moves)
    for raw_move in raw_moves:
        raw_single_move = poke_client.fetch_move_by_url(
            raw_move["move"]["url"])
        if raw_single_move["power"] is not None:
            move = from_api_move_to_move(raw_single_move)
            clean_moves.append(move)
            cnt -= 1

        if cnt == 0:
            break
        elif len(clean_moves) > 9:
            break
        # print("cantidad movimientos:", clean_moves)
    pokemon.asing_moves(clean_moves)

    return pokemon


def get_pokemon_by_ID(id):

    if id < 0 or id is None:
        return None

    raw_pokemon = poke_client.fetch_pokemon_detail_by_id(id)
    if raw_pokemon is None:
        return None
    pokemon_wm = from_api_to_pokemon(raw_pokemon)

    complete_pokemon = get_moves_from_api_individual(pokemon_wm)
    return complete_pokemon

    # return pokemon_repo.search_by_id(id)


# Recibe el ID, y un valor max(propobilidad),
# hará raices cuadradas hasta hacer que el ID sea menor que el máximo
# y lo comparará con un número aleatorio entre 0 y el máximo.


def is_pokemon_shiny(id, max):
    shiny = int(random.randint(0, max))
    while (id > max):
        id = math.trunc(math.sqrt(id))
    if id == shiny:
        return True
    else:
        return False


def get_pokemon_by_name(pokemon_name):
    if pokemon_name:
        pokemons = get_pokemons()

        for pokemon in pokemons:

            if pokemon["name"].lower() == pokemon_name.lower():
                raw_pokemon = poke_client.fetch_pokemon_detail_by_name(
                    pokemon['name'])
                pokemon_without_moves = poke_adaptor.from_api_to_pokemon(
                    raw_pokemon)

                pokemon_complete = get_moves_from_api_individual(
                    pokemon_without_moves)

                return pokemon_complete

    return None


def get_stat_value(pokemon, stat_name):
    searched_stat = None
    for stat in pokemon.stats:
        if stat['name'] == stat_name:
            searched_stat = stat.get('value', 0)
            break
    return searched_stat


if __name__ == "__main__":
    print("Este código execútase cando o script é executado directamente.")

    data = get_list_pokemons(0, 4)
