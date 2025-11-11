from app.models.battle import Battle
import app.repositories.pokemon_repo as pokemon_repo
from app.services.pokemon_service import obtener_valor_stat
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
    random_move = pokemon.moves[random.randint(0, len(pokemon.moves)-1)]
    if (random_move not in moves):
        moves.append(random_move)
    if len(moves) < 4:
        return random_moves(pokemon, moves)
    return moves


def create_battle(my_pokemon, enemy_pokemon, my_pokemon_moves):
    # 0,my_pokemon,enemy_pokemon,'',
    health_player = obtener_valor_stat(my_pokemon, 'hp')
    health_rival = obtener_valor_stat(enemy_pokemon, 'hp')
    moves_rival = random_moves(enemy_pokemon, [])
    battle = Battle(0, my_pokemon, enemy_pokemon, '', health_player,
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
    # Comparamos que pokemon es más rapido para que empiece el
    enemy_move = enemyAttack(enemy_pokemon.moves)
    if enemy_pokemon.stats[5]['value'] > my_pokemon.stats[5]['value']:
        # Funcion que devuelve un ataque aleatorio

        if calculatePrecision:
            # si el ataque acierta
            # battle.log+=f'{ enemy_pokemon.name} ha usado: {enemy_move}'
            writeLog(battle.log, enemy_pokemon, enemy_move)
            damage = calcularPSaRestar(enemy_pokemon, my_pokemon, enemy_move)
            my_pokemon.stats[0]['value'] = restarHP(my_pokemon,damage)
            if not evaluatePokemon(my_pokemon.stats[0]['value']):
                battle.log+=f'{my_pokemon} se ha debilitado. {enemy_pokemon} ha ganado!'
                my_pokemon.stats[0]['value']=0
                return battle.log
            else:
                writeLog(battle.log, my_pokemon, my_move)
                damage = calcularPSaRestar(my_pokemon, enemy_pokemon, my_move)
                enemy_pokemon.stats[0]['value'] = restarHP(my_pokemon,damage)
            if not evaluatePokemon(enemy_pokemon.stats[0]['value']):
                battle.log+=f'{enemy_pokemon} se ha debilitado. {my_pokemon} ha ganado!'
                enemy_pokemon.stats[0]['value']=0
                return battle.log
        else:
            # si falla
            battle.log += 'pero falló/n'
    else:
        # si nuestro pokemon ataca antes
        # battle.log+=f'{ my_pokemon.name} ha usado: {my_move}'
        writeLog(battle.log, my_pokemon, my_move)
        damage = calcularPSaRestar(my_pokemon, enemy_pokemon, my_move)
        enemy_pokemon.stats[0]['value'] = restarHP(my_pokemon,damage)
        if not evaluatePokemon(enemy_pokemon.stats[0]['value']):
            battle.log+=f'{enemy_pokemon} se ha debilitado. {my_pokemon} ha ganado!'
            enemy_pokemon.stats[0]['value']=0
            return battle.log
        else:
            writeLog(battle.log, enemy_pokemon, enemy_move)
            damage = calcularPSaRestar(enemy_pokemon, my_pokemon, enemy_move)
            my_pokemon.stats[0]['value'] = restarHP(my_pokemon,damage)
            if not evaluatePokemon(my_pokemon.stats[0]['value']):
                battle.log+=f'{my_pokemon} se ha debilitado. {enemy_pokemon} ha ganado!'
                my_pokemon.stats[0]['value']=0
                return battle.log
    
def calculatePrecision(move):
    probability = move['accuracy']/10
    random = random.randint(0, 10)
    if probability <= random:
        return True
    else:
        return False


def enemyAttack(moves):
    return moves[random.randint(0, len(moves)-1)]


def writeLog(log, pokemon, move):
    log += f'\n{pokemon.name} ha usado: {move}'
    


def calcularPSaRestar(attacker, reciever, move):
    index_damage = 0
    power = move['power']
    move_type = move['type']
    hp_reciever = reciever.stats[0]['value']
    type_attacker = attacker.types

    if power > hp_reciever:
        index_damage += 1.25
    elif power < hp_reciever:
        index_damage += 1
    else:
        index_damage += 0.75
    if move_type in type_attacker:
        index_damage *= 1.25
    else:
        index_damage *= 0.75
    return power*index_damage


def restarHP(pokemon, damage):
    hp = pokemon.stats[0]['value']-damage
    return hp

def evaluatePokemon(hp):
    if hp>=0:
        return True
    else:
        return False





def rivalSpriteSelector():
    from app.rivals import rivals
    return rivals[random.randint(0, len(rivals)-1)]
