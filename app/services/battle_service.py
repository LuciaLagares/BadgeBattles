from app.models.battle import Battle
import app.repositories.pokemon_repo as pokemon_repo
import random


def enemyPokemonSelector(my_pokemon):
    pokemons = pokemon_repo.obtener_pokemons()
    randomPokemonNumber = random.randint(0, len(pokemons)-1)
    enemy_pokemon = pokemons[randomPokemonNumber]
    if len(pokemons) >= 2:
        if (enemy_pokemon.id == my_pokemon.id):
            return enemyPokemonSelector(my_pokemon)
    return enemy_pokemon

def random_moves(pokemon, moves):
    random_move= pokemon.moves[random.randint(0,len(pokemon.moves)-1)]
    if(random_move not in moves):
        moves.append(random_move)
    if len(moves)<4:
        return random_moves(pokemon, moves)
    return moves

def createBattle(my_pokemon,enemy_pokemon,my_pokemon_moves):
    # 0,my_pokemon,enemy_pokemon,'',
    health_player=my_pokemon.stats[0]['value']-10
    health_rival=enemy_pokemon.stats[0]['value']
    moves_rival=random_moves(enemy_pokemon,[])
    battle=Battle(0,my_pokemon,enemy_pokemon,'hola',health_player,health_rival,my_pokemon_moves, moves_rival)
    
    return battle
    




def rivalSpriteSelector():
    from app.rivals import rivals
    return rivals[random.randint(0, len(rivals)-1)]
