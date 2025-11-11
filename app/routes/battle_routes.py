
from flask import Blueprint, redirect, render_template, request, session, url_for
import logging
from app.colors import colors
from app.services import battle_service
logging.basicConfig(level=logging.DEBUG)
battle_bp = Blueprint('battle', __name__, template_folder='templates')


@battle_bp.route("/", methods=['GET', 'POST'])
def pokemon_battle():
    resultado=None
    if request.method == 'GET':
        my_pokemon = session.get('pokemon_selected')
        my_pokemon_moves = session.get('my_pokemon_moves')
        enemy_pokemon = session.get('enemy_pokemon')
        session['battle'] = battle_service.create_battle(
            my_pokemon, enemy_pokemon, my_pokemon_moves)
        return render_template("pokemon_battle.html", colors=colors)
    elif request.method == 'POST':
        option = int(request.form.get('opcion'))
    
        resultado=battle_service.attack(session.get('battle'),option)
        if resultado==-1:
            
            looser=session['battle'].data_pokemon_player.name
            winner=session['battle'].data_pokemon_rival.name
            turnos=session['battle'].turno
            session.pop('battle',None)
            return render_template("pokemon_winner.html",winner=winner,looser=looser,turnos=turnos, colors=colors)
            
        elif resultado==1:
            looser=session['battle'].data_pokemon_rival.name
            winner=session['battle'].data_pokemon_player.name
            turnos=session['battle'].turno
            session.pop('battle',None)
            return render_template("pokemon_winner.html",winner=winner,looser=looser,turnos=turnos, colors=colors)
        
        else:
            return render_template("pokemon_battle.html", colors=colors)
    
        # redirect(url_for("battle.pokemon_battle"))
