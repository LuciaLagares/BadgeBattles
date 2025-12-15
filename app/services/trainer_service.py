from app.database.db import db
from app.models.exceptions import TrainerAlreadyExistException, TrainerNotFound, WrongPassword
from app.models.trainer import Trainer

from app.repositories.trainer_repo import create_trainer, get_trainer_by_id, get_trainer_by_name


def register_trainer(name, password, gender):
    trainer = get_trainer_by_name(name)
    if gender=='male':
        sprite='images/character_sprite/male_character.png'
    else:
        sprite='images/character_sprite/female_character.png'
    if trainer is not None:
        raise TrainerAlreadyExistException()

    return create_trainer(name, password, gender,sprite)


def authenticate_trainer(name, password):

    trainer = get_trainer_by_name(name)
    if trainer is None:
        raise TrainerNotFound()

    if not trainer.check_password(password):
        raise WrongPassword()

    return trainer


def get_trainer_by_id_service(id):
    trainer=get_trainer_by_id(id)
    if trainer:
        return trainer
    return None

def add_opponets_service():
    rivals=[
        {
            'name': 'Iker Jimenez',
            'sprite': 'images/rival_sprite/Iker.webp',
            'gender': 'male'        
        },
        {
            'name': 'Cristiano Ronaldo',
            'sprite': 'images/rival_sprite/Cristiano.webp',
            'gender': 'male'
        },
        {
            'name': 'Alvaro Alfarero',
            'sprite': 'images/rival_sprite/Abascal.webp',
            'gender': 'male'
        },
        {
            'name': 'Estudiante DAW',
            'sprite': 'images/rival_sprite/Estudiante.webp',
            'gender': 'male'
        },
        {
            'name': 'Rey Pokemon',
            'sprite': 'images/rival_sprite/Felipe_VI.webp',
            'gender':'male'
        },
    
        {
            'name': 'Guiri',
            'sprite': 'images/rival_sprite/Guiri.webp',
            'gender':'male'
        },
        {
            'name': 'Ignatius',
            'sprite': 'images/rival_sprite/Ignatius.webp',
            'gender':'male'
        },
        {
            'name': 'C++ Programmer',
            'sprite': 'images/rival_sprite/Programador.webp',
            'gender':'male'
        },
        {
            'name': 'Presidente Johto',
            'sprite': 'images/rival_sprite/Pedro_Sanchez.webp',
            'gender':'male'
        },
        {
            'name': 'SalaryMan',
            'sprite': 'images/rival_sprite/Rajoy.webp',
            'gender':'male'
        }

    ]
    for rival in rivals:
        create_trainer(name=rival['name'], password='0000',
                   sprite=rival['sprite'], gender=rival['gender'])
