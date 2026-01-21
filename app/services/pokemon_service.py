from app.clients.adaptor.poke_adaptor import from_api_to_pokemon, from_api_to_pokemon_list
import app.repositories.pokemon_repo as pokemon_repo
import app.clients.poke_client as poke_client
import random
import math


# def get_pokemons():
#     return pokemon_repo.get_pokemons()

def get_pokemons():
    # Este busca todos los pokemons para poder elegir el pokemon rival aleatoriamente
    URL = "https://pokeapi.co/api/v2/pokemon"
    # data = poke_client.fetch_all_pokemon(0,8)


def get_list_pokemons(offset, limit):
    # Para listar pokemons para elegir
    data = poke_client.fetch_all_pokemon(offset, limit)
    if data is None:

        return None
    list_pokemons = data["results"]
    if list_pokemons is None:

        return None
    urls = []
    for item_pokemon in list_pokemons:
        urls.append(item_pokemon["url"])

    raw_pokemons = poke_client.fetch_pokemons_parallel(urls)
    if raw_pokemons is None:

        return None

    pokemons = from_api_to_pokemon_list(raw_pokemons)
    
    return pokemons




def get_pokemon_by_ID(id):

    if id < 0 or id is None:
        return None

    return pokemon_repo.search_by_id(id)

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

            if pokemon.name.lower() == pokemon_name.lower():
                return pokemon
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
    print(data)
