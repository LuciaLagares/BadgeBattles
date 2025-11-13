import math
from app.models.battle import Battle
import app.repositories.pokemon_repo as pokemon_repo
from app.services.pokemon_service import get_stat_value
import random


def enemy_pokemon_selector(my_pokemon):
    pokemons = pokemon_repo.get_pokemons()
    randomPokemonNumber = random.randint(0, len(pokemons)-1)
    enemy_pokemon = pokemons[randomPokemonNumber]
    if len(pokemons) >= 2:
        if (enemy_pokemon.id == my_pokemon.id):
            return enemy_pokemon_selector(my_pokemon)
    return enemy_pokemon


def random_moves(pokemon, moves):
    random_move = pokemon.moves[random.randint(0, len(pokemon.moves)-1)]
    if (random_move not in moves):
        moves.append(random_move)
    if len(moves) < 4:
        return random_moves(pokemon, moves)
    return moves


def create_battle(my_pokemon, enemy_pokemon, my_pokemon_moves):

    health_player = get_stat_value(my_pokemon, 'hp')
    health_rival = get_stat_value(enemy_pokemon, 'hp')
    moves_rival = random_moves(enemy_pokemon, [])
    battle = Battle(0, my_pokemon, enemy_pokemon, [], health_player,
                    health_rival, my_pokemon_moves, moves_rival)

    return battle


def attack(battle, option):
    # Avanzamos el turno
    battle.turno += 1
    # Declaramos los pokemon con nombre propio para que sea más comodo trabajar
    my_pokemon = battle.data_pokemon_player
    enemy_pokemon = battle.data_pokemon_rival

    # Obtenemos el movimiento desde la opcion pulsada
    my_move = battle.moves_player[option]
    # Funcion que devuelve un ataque aleatorio
    enemy_move = enemy_attack(enemy_pokemon.moves)
    # Comparamos que pokemon es más rapido para que empiece el combate
    if enemy_pokemon.stats[5]['value'] >= my_pokemon.stats[5]['value']:
        # Si el enemigo es más rápido
        if calculate_precision(enemy_move):
            # si el ataque acierta
            damage = calculate_HP_to_substract(
                enemy_pokemon, my_pokemon, enemy_move)
            my_pokemon.stats[0]['value'] = substract_HP(my_pokemon, damage)
            write_log(battle, enemy_pokemon, enemy_move, damage, my_pokemon)
        else:
            # si falla
            miss_log(battle, enemy_pokemon, enemy_move)

            # Si falla el ataque, el otro pokemon va a tener toda la vida, por lo que no va entrar en el if.
        if not evaluate_pokemon(my_pokemon.stats[0]['value']):
            winner_log(battle, enemy_pokemon, my_pokemon)
            my_pokemon.stats[0]['value'] = 0
            return -1  # termina el turno-------------------------------------------
        else:
            if calculate_precision(my_move):
                damage = calculate_HP_to_substract(
                    my_pokemon, enemy_pokemon, my_move)
                enemy_pokemon.stats[0]['value'] = substract_HP(
                    enemy_pokemon, damage)
                write_log(battle, my_pokemon, my_move, damage, enemy_pokemon)
            else:
                miss_log(battle, my_pokemon, my_move)
            if not evaluate_pokemon(enemy_pokemon.stats[0]['value']):
                winner_log(battle, my_pokemon, enemy_pokemon)
                enemy_pokemon.stats[0]['value'] = 0
                return 1  # termina el turno-------------------------------------------

    else:
        # si nuestro pokemon ataca antes
        if calculate_precision(my_move):
            damage = calculate_HP_to_substract(
                my_pokemon, enemy_pokemon, my_move)
            enemy_pokemon.stats[0]['value'] = substract_HP(
                enemy_pokemon, damage)
            write_log(battle, my_pokemon, my_move, damage, enemy_pokemon)
        else:
            miss_log(battle, my_pokemon, my_move)

        if not evaluate_pokemon(enemy_pokemon.stats[0]['value']):
            winner_log(battle, my_pokemon, enemy_pokemon)
            enemy_pokemon.stats[0]['value'] = 0
            return 1  # termina el turno
        else:
            if calculate_precision(enemy_move):
                damage = calculate_HP_to_substract(
                    enemy_pokemon, my_pokemon, enemy_move)
                my_pokemon.stats[0]['value'] = substract_HP(my_pokemon, damage)
                write_log(battle, enemy_pokemon,
                          enemy_move, damage, my_pokemon)
            else:
                miss_log(battle, enemy_pokemon, enemy_move)
            if not evaluate_pokemon(my_pokemon.stats[0]['value']):
                winner_log(battle, enemy_pokemon, my_pokemon)
                my_pokemon.stats[0]['value'] = 0
                return -1  # termina el turno


def calculate_precision(move):
    probability = move['accuracy']/10
    random_number = random.randint(1, 10)
    if probability >= random_number:
        return True
    else:
        return False


def enemy_attack(moves):
    return moves[random.randint(0, len(moves)-1)]


def write_log(battle, attacker, move, damage, reciever):
    battle.log.append(
        f'{attacker} ha usado: {move['name'].capitalize()} con un daño de {math.floor(damage)}, dejando a {reciever} con {reciever.stats[0]['value']} de vida.')


def miss_log(battle, attacker, move):
    battle.log.append(
        f' {attacker} intento hacer {move['name'].capitalize()} pero falló.')


def winner_log(battle, winner, looser):
    battle.log.append(
        f'{looser} se ha debilitado. {winner} ha ganado!')


def calculate_HP_to_substract(attacker, reciever, move):
    index_damage = 0
    power = move['power']
    move_type = move['type']
    defense_reciever = reciever.stats[2]['value']
    type_attacker = attacker.types

    if power > defense_reciever:
        index_damage += 1.15
    elif power == defense_reciever:
        index_damage += 1
    else:
        index_damage += 0.75
    if move_type in type_attacker:
        index_damage *= 1.10
    else:
        index_damage *= 0.80
    return power/2*index_damage


def substract_HP(pokemon, damage):
    hp = pokemon.stats[0]['value']-damage
    return int(hp)


def evaluate_pokemon(hp):
    if hp > 0:
        return True
    else:
        return False


def rivalSpriteSelector():
    from app.rivals import rivals
    return rivals[random.randint(0, len(rivals)-1)]
