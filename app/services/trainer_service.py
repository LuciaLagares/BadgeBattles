from app.database.db import db
from app.models.trainer import Trainer

from app.repositories.trainer_repo import create_trainer, get_all_trainers



def register_trainer(name, password, gender):
    # Pide todos los trainers
    # try:
    # trainers=get_all_trainers()
    # # Compara por nombre
    # if trainers:
    #     for trainer in trainers:
    #         if trainer.name==name:
    #             print('EL ENTRENADOR YA EXISTE')    
    #             break
            
    # y lanza excepcion si existe
    

    return create_trainer(name,password,gender)


    # except:
    #     pass

def authenticate_trainer():
    pass