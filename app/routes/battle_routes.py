
from flask import Blueprint, render_template, request, session
import logging
from app.colors import colors
from app.services import battle_service
logging.basicConfig(level=logging.DEBUG)
battle_bp = Blueprint('battle', __name__, template_folder='templates')

@battle_bp.route("/")
def pokemon_battle():
    
    my_pokemon =session.get('pokemon_selected')
    my_pokemon_moves = battle_service.random_moves(my_pokemon, [])
    session['my_pokemon_moves']=my_pokemon_moves
    enemy_pokemon = None
    enemy_pokemon = battle_service.enemyPokemonSelector(my_pokemon)
    session['enemy_pokemon']=enemy_pokemon

    # enemy_moves = battle_service.random_moves(enemy_pokemon, [])
    rival = battle_service.rivalSpriteSelector()
    session['rival']=rival
    session['battle']=battle_service.create_battle(my_pokemon,enemy_pokemon,my_pokemon_moves)
    print('---------------------------',session['battle'].health_player,type (session['battle'].health_player),'-----------------------------------------')

    return render_template("pokemon_battle.html", colors=colors)
