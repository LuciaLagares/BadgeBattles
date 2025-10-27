import json
from app.models.pokemon import Pokemon
from pathlib import Path


with open(Path("data/data.json"), encoding="utf-8") as fichero_data:
    _POKEMONS = json.load(fichero_data)
    
def obtener_pokemons():
    pokemons = []
    
    for p in _POKEMONS:
        pokemon = Pokemon(
            id=p['id'],
            name=p['name'],
            height=p['height'],
            weight=p['weight'],
            moves=p['moves'],
            sprites=p['sprites'],
            stats=p['stats'],
            types=p['types']
        ) 
        pokemons.append(pokemon)
    return pokemons

def buscar_por_id(id):
    pokemons = obtener_pokemons()
    pokemon_a_buscar = None
    for p in pokemons:
        if p.id == id:
            pokemon_a_buscar = p
            break
    return pokemon_a_buscar
