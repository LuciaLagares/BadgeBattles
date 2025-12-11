from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.db import db


class BattleDB(db.Model):

    __tablename__ = 'Battle'
    id = Column(Integer, autoincrement=True, primary_key=True)
    attacker_pokemon = Column(Integer, nullable=False)
    defender_pokemon = Column(Integer, nullable=False)
    result = Column(String(100), nullable=False)
    date = Column(DateTime, default=datetime.now, nullable=False)
    attacker_id = Column(Integer, ForeignKey(
        "TrainerDB.id", ondelete="CASCADE"), nullable=False)
    defender_id = Column(Integer, ForeignKey(
        "TrainerDB.id", ondelete="CASCADE"), nullable=False)
    attacker = relationship(
        "Trainer",
        back_populates="battle_as_attacker",
        foreign_keys=[attacker_id]
    )
    defender = relationship(
        "Trainer",
        back_populates="battle_as_defender",
        foreign_keys=[defender_id]
    )

    def __init__(self, attacker_id, defender_id, attacker_pokemon_id, defender_pokemon_id, result, date):
        super().__init__()
        self.attacker_pokemon = attacker_pokemon_id
        self.defender_pokemon = defender_pokemon_id
        self.attacker_id = attacker_id
        self.defender_id = defender_id
        self.result = result
        self.date = date
