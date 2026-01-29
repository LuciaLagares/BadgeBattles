import math
from operator import indexOf
from app.models.battle import Battle
import app.repositories.pokemon_repo as pokemon_repo
from app.repositories.trainer_repo import get_all_trainers
from app.services.pokemon_service import get_pokemons, get_stat_value
import random


def enemy_pokemon_selector(my_pokemon):
    pokemons = get_pokemons()
    randomPokemonNumber = random.randint(0, len(pokemons)-1)
    enemy_pokemon = pokemons[randomPokemonNumber]
    if len(pokemons) >= 2:
        if (enemy_pokemon["name"] == my_pokemon.name):
            return enemy_pokemon_selector(my_pokemon)
    return enemy_pokemon


def random_moves(pokemon, moves):
    if len(pokemon.moves) == 0:
        return [{
            "name": "struggle",
            "accuracy": 100,
            "power": 10,
            "type": "normal"
        }]
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


def attack_battle(battle, option):
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

        if attack(enemy_pokemon, my_pokemon, enemy_move, battle):
            return enemy_pokemon, my_pokemon
        else:
            if attack(my_pokemon, enemy_pokemon, my_move, battle):
                return my_pokemon, enemy_pokemon
    else:
        if attack(my_pokemon, enemy_pokemon, my_move, battle):
            return my_pokemon, enemy_pokemon
        else:
            if attack(enemy_pokemon, my_pokemon, enemy_move, battle):
                return enemy_pokemon, my_pokemon
    return False, False


def attack(attacker, reciever, attacker_move, battle):
    if calculate_precision(attacker_move):
        # si el ataque acierta
        damage = calculate_HP_to_substract(
            attacker, reciever, attacker_move)
        reciever.stats[0]['value'] = substract_HP(reciever, damage)
        write_log(battle, attacker, attacker_move, damage, reciever)
    else:
        # si falla
        miss_log(battle, attacker, attacker_move)

        # Si falla el ataque, el otro pokemon va a tener toda la vida, por lo que no va entrar en el if.
    if not evaluate_pokemon(reciever.stats[0]['value']):
        winner_log(battle, attacker, reciever)
        reciever.stats[0]['value'] = 0
        return True  # termina el turno-------------------------------------------
    return False
# si devuelve un booleano con true es que ha ganado


def calculate_precision(move):
    if move["accuracy"] is None:
        return True
    probability = move['accuracy']/10
    random_number = random.randint(1, 10)
    if probability >= random_number:
        return True
    else:
        return False


def enemy_attack(moves):
    if(len(moves)==0):
        return {
            "name": "struggle",
            "accuracy": 100,
            "power": 10,
            "type": "normal"
        }
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
    if hp<=0:
        hp=0
    return int(hp)


def evaluate_pokemon(hp):
    if hp > 0:
        return True
    else:
        return False


def rivalSpriteSelector(trainer_id):
    rivals = get_all_trainers()
    rivals_without_trainer = []
    for rival in rivals:
        if rival.id == trainer_id:
            continue
        rivals_without_trainer.append(rival)
    return rivals_without_trainer[random.randint(0, len(rivals_without_trainer)-1)]


def battle_result(winner_id, attacker_pokemon_id):
    """Recibe la ID del pokemon ganador y la compara con el id del pokemon atacante"""
    if winner_id == attacker_pokemon_id:
        return True
    else:
        return False
