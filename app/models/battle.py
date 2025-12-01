from sqlalchemy import Column, Date, Integer, String
from app.database import db
from app.models.pokemon import Pokemon


class Battle(db.Model):
    __tablename__='BattleDB'
    
    id=Column(Integer, autoincrement=True,primary_key=True)
    trainer1_id=Column(Integer, nullable=False)
    trainer2_id=Column(Integer, nullable=False)
    trainer1_pokemon=Column(String(100), nullable=False)
    trainer2_pokemon=Column(String(100), nullable=False)
    date=Date()
    resultado=Column(String(100), nullable=False)
    
    

    def __init__(self, turno, data_pokemon_player, data_pokemon_rival, log, health_player, health_rival, moves_player, moves_rival):

        self.turno = turno
        self.data_pokemon_player = data_pokemon_player
        self.data_pokemon_rival = data_pokemon_rival
        self.log = log
        self.health_player = health_player
        self.health_rival = health_rival
        self.moves_player = moves_player
        self.moves_rival = moves_rival

    
    def to_dict(self):
        battle = {
            "turno": self.turno,
            "data_pokemon_player": self.data_pokemon_player.to_dict(),
            "data_pokemon_rival": self.data_pokemon_rival.to_dict(),
            "log": self.log,
            "health_player": self.health_player,
            "health_rival": self.health_rival,
            "moves_player": self.moves_player,
            "moves_rival": self.moves_rival,
        }
        return battle
    @staticmethod
    def from_dict(dict):
        pokemon_player=Pokemon.from_dict(dict["data_pokemon_player"])
        pokemon_rival=Pokemon.from_dict(dict["data_pokemon_rival"])
        return Battle(
            dict['turno'],
            pokemon_player,
            pokemon_rival,
            dict['log'],
            dict['health_player'],
            dict['health_rival'],
            dict['moves_player'],
            dict['moves_rival']
        )
        