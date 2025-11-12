
from flask import Blueprint, redirect, render_template, request, session, url_for
import logging
from app.colors import colors
from app.decorators import login_required
from app.services import battle_service
logging.basicConfig(level=logging.DEBUG)
battle_bp = Blueprint('battle', __name__, template_folder='templates')


@battle_bp.route("/", methods=['GET', 'POST'])
@login_required
def pokemon_battle():
    resultado = None
    my_pokemon = None
    my_pokemon_moves = None
    enemy_pokemon = None
    if request.method == 'GET':
        my_pokemon = session.get('pokemon_selected')
        my_pokemon_moves = session.get('my_pokemon_moves')
        enemy_pokemon = session.get('enemy_pokemon')
        if my_pokemon and my_pokemon_moves and enemy_pokemon:
            session['battle'] = battle_service.create_battle(
                my_pokemon, enemy_pokemon, my_pokemon_moves)
            return render_template("pokemon_battle.html", colors=colors)
        else:
            return redirect(url_for("pokemon.pokemon_list"))
    elif request.method == 'POST':
        option = int(request.form.get('opcion'))
        if not session.get('battle'):
            return redirect(url_for("pokemon.pokemon_list"))
        resultado = battle_service.attack(session.get('battle'), option)
        
        if resultado == -1:

            looser = session['battle'].data_pokemon_player.name
            winner = session['battle'].data_pokemon_rival


        elif resultado == 1:
            looser = session['battle'].data_pokemon_rival.name
            winner = session['battle'].data_pokemon_player
            
        else:
            return render_template("pokemon_battle.html", colors=colors)
        turnos = session['battle'].turno
        logHistoric = session['battle'].log
        session.pop('battle', None)
        session.pop('pokemon_selected', None)
        session.pop('enemy_pokemon', None)
        return render_template("pokemon_winner.html", winner=winner, looser=looser, turnos=turnos, logList=logHistoric, colors=colors)

        # redirect(url_for("battle.pokemon_battle"))
