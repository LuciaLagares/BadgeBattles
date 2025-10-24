import repositories.pokemon_repo as pokemon_repo
import random
import math


def listar_pokemons():
    return pokemon_repo.obtener_pokemons()


def obtener_pokemon_por_ID(id):
    if id < 0 or id is None:
        return None

    return pokemon_repo.buscar_por_id(id)


def is_pokemon_shiny(id, max):
        shiny = int(random.randint(0, max))
        while (id > max):
            id = math.trunc(math.sqrt(id))
        if id == shiny:
            return True
        else:
            return False

