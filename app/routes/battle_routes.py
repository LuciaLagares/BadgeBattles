import datetime
import random
from flask import Blueprint, current_app, jsonify, redirect, render_template, request

from app import colors
from app.services import battle_service, pokemon_service

battle_bp = Blueprint('battle', __name__, template_folder='templates')

@battle_bp.route("/")
def pokemon_battle():
    #  year=year, my_pokemon=pokemon_found, trainer=trainer, colors=colors
    year = request.args.get('year')
    my_pokemon_id = int(request.args.get('pokemon_found_id'))
    trainer = request.args.get('trainer')
    gender = request.args.get('gender')
    enemy_pokemon = None
    my_pokemon = pokemon_service.obtener_pokemon_por_ID(my_pokemon_id)

    random_moves = battle_service.random_moves(my_pokemon, [])

    enemy_pokemon = battle_service.enemyPokemonSelector(my_pokemon)


    def rivalSpriteSelector():
         # Rival Dict
        from app.rivals import rivals
        return rivals[random.randint(0, len(rivals)-1)]

    
    rival = rivalSpriteSelector()
  

    return render_template("pokemon_battle.html", year=year, my_pokemon=my_pokemon, enemy_pokemon=enemy_pokemon, trainer=trainer, colors=colors, rival=rival, gender=gender, moves=random_moves)