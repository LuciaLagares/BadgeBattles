import datetime
import random
from flask import Blueprint, current_app, jsonify, redirect, render_template, request
import logging
from app.colors import colors
from app.services import battle_service, pokemon_service
logging.basicConfig(level=logging.DEBUG)
battle_bp = Blueprint('battle', __name__, template_folder='templates')

@battle_bp.route("/")
def pokemon_battle():
    #  year=year, my_pokemon=pokemon_found, trainer=trainer, colors=colors
    year = request.args.get('year')
    my_pokemon_name = request.args.get('pokemon')
    trainer = request.args.get('trainer')
    gender = request.args.get('gender')
    enemy_pokemon = None
    # my_pokemon = pokemon_service.obtener_pokemon_por_nombre(my_pokemon_name)
    my_pokemon = pokemon_service.obtener_pokemon_por_nombre(my_pokemon_name) 

    random_moves = battle_service.random_moves(my_pokemon, [])

    enemy_pokemon = battle_service.enemyPokemonSelector(my_pokemon)


    def rivalSpriteSelector():
         # Rival Dict
        from app.rivals import rivals
        return rivals[random.randint(0, len(rivals)-1)]

    
    rival = rivalSpriteSelector()
  

    return render_template("pokemon_battle.html", my_pokemon=my_pokemon, enemy_pokemon=enemy_pokemon, colors=colors, rival=rival, moves=random_moves)