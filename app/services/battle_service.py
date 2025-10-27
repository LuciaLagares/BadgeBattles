import app.repositories.pokemon_repo as pokemon_repo
import random

def enemyPokemonSelector(my_pokemon):
    pokemons = pokemon_repo.obtener_pokemons()
    randomPokemonNumber = random.randint(0, len(pokemons)-1)
    enemy_pokemon = pokemons[randomPokemonNumber]
    if len(pokemons) >= 2:
        if (enemy_pokemon.id == my_pokemon.id):
            return enemyPokemonSelector()
    return enemy_pokemon

def random_moves(pokemon, moves):
    random_move= pokemon.moves[random.randint(0,len(pokemon.moves)-1)]
    if(random_move not in moves):
        moves.append(random_move)
    if len(moves)<4:
        return random_moves(pokemon, moves)
    return moves
