
from app.database.db import db
from app.models.battleDB import BattleDB


def create_battleDB(attacker_id, defender_id, attacker_pokemon, defender_pokemon, result, date):

    battle = BattleDB(attacker_id=attacker_id, defender_id=defender_id,
                      attacker_pokemon_id=attacker_pokemon, defender_pokemon_id=defender_pokemon, result=result, date=date)
    db.session.add(battle)
    db.session.commit()
    return battle


def get_battle_by_id(id_db):
    battle = BattleDB.query.filter_by(id=id_db).first()
    if battle:
        return battle
    return None

def get_all_battles_id(id_db):

    battles=BattleDB.query.filter((BattleDB.attacker_id==id_db) | (BattleDB.defender_id==id_db)).all()
    if battles:
        return battles
    return None

def get_battle_attacker(id_db):
    battles = BattleDB.query.filter_by(attacker_id=id_db).all()
    # Comprobar en service si obtiene array vacío
    return battles


def delete_battle(battle):
    db.session.delete(battle)
    db.session.commit()
    return True
