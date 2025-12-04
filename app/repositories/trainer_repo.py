
from app.database.db import db
from app.models.trainer import Trainer


def create_trainer(name,password,gender):
    
    trainer=Trainer(name,password,gender)
    db.session.add(trainer)
    db.session.commit()
    return trainer
    
def get_trainer_by_name(name_db):
    trainer=Trainer.query.filter_by(name=name_db).first()
    if trainer:
        return trainer
    return None
def get_trainer_by_id(id_db):
    trainer=Trainer.query.filter_by(id=id_db).first()
    if trainer:
        return trainer
    return None

def get_all_trainers():
    trainers=Trainer.query.all()
    if trainers:
        return trainers
    return None

    