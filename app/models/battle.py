from datetime import datetime
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from app.database.db import db
from app.models.pokemon import Pokemon
from sqlalchemy import relationship



class Battle(db.Model):
    __tablename__='BattleDB'
    
    id=Column(Integer, autoincrement=True,primary_key=True)
    trainer1_pokemon=Column(Integer, nullable=False)
    trainer2_pokemon=Column(Integer, nullable=False)
    resultado=Column(String(100), nullable=False)
    date=Column(DateTime, default=datetime.now, nullable=False)
    trainer1_id=Column(Integer, ForeignKey("TrainerDB.id", ondelete="CASCADE"), nullable=False)
    trainer2_id=Column(Integer, nullable=False)
    
    
    trainers=relationship("Trainer" ,back_populates='battles', passive_deletes=True)
    
    

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
        