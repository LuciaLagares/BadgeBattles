from app.database.db import db
from app.models.exceptions import TrainerAlreadyExistException, TrainerNotFound, WrongPassword
from app.models.trainer import Trainer

from app.repositories.trainer_repo import create_trainer, get_trainer_by_name



def register_trainer(name, password, gender):
    trainer=get_trainer_by_name(name)

    if trainer is not None:
        raise TrainerAlreadyExistException()

    return create_trainer(name,password,gender)


def authenticate_trainer(name,password):

    trainer=get_trainer_by_name(name)
    if trainer is None:
        raise TrainerNotFound()
    
    if not trainer.check_password(password):
        raise WrongPassword()
    
    return trainer
    
    