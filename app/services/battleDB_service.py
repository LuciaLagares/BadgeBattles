from datetime import datetime
from app.repositories.battle_repo import create_battleDB


def create_battle_service(
    attacker_id,
    defender_id,
    attacker_pokemon_id,
    defender_pokemon_id,
    result):
    fecha=datetime.now()

    create_battleDB(attacker_id=attacker_id,defender_id=defender_id,attacker_pokemon=attacker_pokemon_id,defender_pokemon=defender_pokemon_id,result=result,date=fecha)   