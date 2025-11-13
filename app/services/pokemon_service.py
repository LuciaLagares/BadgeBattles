import app.repositories.pokemon_repo as pokemon_repo
import random
import math


def get_pokemons():
    return pokemon_repo.get_pokemons()


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


def get_stat_value(pokemon, stat_name):
    searched_stat = None
    for stat in pokemon.stats:
        if stat['name'] == stat_name:
            searched_stat = stat.get('value', 0)
            break
    return searched_stat
