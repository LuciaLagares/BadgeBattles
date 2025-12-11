import json
from app.models.pokemon import Pokemon
from pathlib import Path

DATA_PATH=Path(__file__).parent.parent.parent /"data"/"data.json"

# with open(Path("data/data.json"), encoding="utf-8") as fichero_data:
with open(DATA_PATH, encoding="utf-8") as fichero_data:
    _POKEMONS = json.load(fichero_data)


def get_pokemons():
    pokemons = []

    for p in _POKEMONS:
        pokemon = Pokemon(**p)
        pokemons.append(pokemon)
    return pokemons


def search_by_id(id):
    pokemons = get_pokemons()
    pokemon_searched = None
    for p in pokemons:
        if p.id == id:
            pokemon_searched = p
            break
    return pokemon_searched
