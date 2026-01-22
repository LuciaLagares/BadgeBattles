

from app.models.pokemon import Pokemon


def from_api_to_pokemon_list(api_pokemons):
    pokemons=[]
    for api_pokemon in api_pokemons:
        pokemon=from_api_to_pokemon(api_pokemon)
        pokemons.append(pokemon)
    return pokemons

def from_api_to_pokemon(api_pokemon):
    cleaned_stats = from_api_stats_to_stats(api_pokemon)
    cleaned_sprites = from_api_sprites_to_sprites(api_pokemon['sprites'])
    cleaned_types=from_api_types_to_types(api_pokemon['types'])
    
    #Tenemos el raw pokemon, con el cual tenemos acceso a todos los movimientos, 
    # lo que haremos es recorrer el array de movimientos para enviarle cada ataque a un metodo que lo busque contra la api y compruebe si hace daño
    # si hace daño nos devolvera un diccionario, asi hasta juntar 8.
     
    pokemon_dict = {
        "id": api_pokemon["id"],
        "name": api_pokemon["name"],
        "weight": api_pokemon["weight"],
        "height": api_pokemon["height"],
        "stats": cleaned_stats,
        "sprites": cleaned_sprites,
        "moves": "",
        "types": cleaned_types
    }
    # Hay que quitarlo
    pokemon=Pokemon.from_dict(pokemon_dict)

    return pokemon


def from_api_stats_to_stats(api_pokemon):
    cleaned_stats = []
    raw_stats = api_pokemon["stats"]
    for raw_stat in raw_stats:
        stat = {
            "name": raw_stat["stat"]["name"],
            "value": raw_stat["base_stat"]
        }
        cleaned_stats.append(stat)
    return cleaned_stats



def from_api_sprites_to_sprites(sprites):
    cleaned_sprites = {
        "front_default": sprites["front_default"],
        "back_default": sprites["back_default"],
        "front_shiny": sprites["front_shiny"],
        "back_shiny": sprites["back_shiny"]
    }
    return cleaned_sprites


def from_api_types_to_types(types):
    cleaned_types=[]
    for type in types:
        cleaned_types.append(type["type"]["name"])
    return cleaned_types

def from_api_move_to_move(move):
    
    cleaned_move={
        "name":move["name"],
        "url":None,
        "accuracy":move["accuracy"],
        "power":move["power"],
        "type":move["type"]["name"]
    }
    return cleaned_move
    


    