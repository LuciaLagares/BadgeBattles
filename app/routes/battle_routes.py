
from flask import Blueprint, render_template, request, session
import logging
from app.colors import colors
from app.services import battle_service
logging.basicConfig(level=logging.DEBUG)
battle_bp = Blueprint('battle', __name__, template_folder='templates')


@battle_bp.route("/", methods=['GET', 'POST'])
def pokemon_battle():
    if request.method == 'GET':
        my_pokemon = session.get('pokemon_selected')
        my_pokemon_moves = session.get('my_pokemon_moves')
        enemy_pokemon = session.get('enemy_pokemon')
        session['battle'] = battle_service.create_battle(
            my_pokemon, enemy_pokemon, my_pokemon_moves)
        return render_template("pokemon_battle.html", colors=colors)
    elif request.method == 'POST':
        option = int(request.form.get('opcion'))
        print('-------------------------------',
              option, '------------------------------')
        battle_service.attack(session.get('battle'),option)
        return render_template("pokemon_battle.html", colors=colors)
