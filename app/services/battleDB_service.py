from datetime import datetime
from app.repositories.battle_repo import create_battleDB, delete_battle, get_all_battles_id, get_battle_by_id


def create_battle_service(
    attacker_id,
    defender_id,
    attacker_pokemon_id,
    defender_pokemon_id,
    result):
    fecha=datetime.now()

    create_battleDB(attacker_id=attacker_id,defender_id=defender_id,attacker_pokemon=attacker_pokemon_id,defender_pokemon=defender_pokemon_id,result=result,date=fecha)   
    
def get_all_battles_details(trainer_id):
    battles=get_all_battles_id(trainer_id)
    if battles:
        return  battles
    
    return None
    
def get_single_battle_by_id(battle_id):
    battle=get_battle_by_id(battle_id)
    if battle:
        return battle
    return None

def delete_battle_by_id(battle_id):
    battle=get_single_battle_by_id(battle_id)
    if battle:
        delete_battle(battle=battle)
    