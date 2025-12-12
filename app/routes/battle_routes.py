
from flask import Blueprint, redirect, render_template, request, session, url_for
import logging


from app.colors import colors
from app.decorators import login_required
from app.models.battle import Battle
from app.models.pokemon import Pokemon
from app.services import battle_service
from app.services.battleDB_service import create_battle_service
logging.basicConfig(level=logging.DEBUG)
battle_bp = Blueprint('battle', __name__, template_folder='templates')


@battle_bp.route("/", methods=['GET', 'POST'])
@login_required
def pokemon_battle():
    my_pokemon = None
    my_pokemon_moves = None
    enemy_pokemon = None
    if request.method == 'GET':
        
        my_pokemon_dict = session.get('pokemon_selected')
        
        if my_pokemon_dict is None:
            return render_template("pokemon.pokemon_list", error='No Pokemon was selected')
        my_pokemon=Pokemon.from_dict(my_pokemon_dict)
       
      
        my_pokemon_moves = session.get('my_pokemon_moves')
        enemy_pokemon_dict = session.get('enemy_pokemon')
        if enemy_pokemon_dict is None:
            return render_template("pokemon.pokemon_list", error='No enemy Pokemon was selected')
        enemy_pokemon=Pokemon.from_dict(enemy_pokemon_dict)
        if my_pokemon and my_pokemon_moves and enemy_pokemon:
            
            battle_dict= battle_service.create_battle(
                my_pokemon, enemy_pokemon, my_pokemon_moves).to_dict()
            if battle_dict is None:
                return render_template("pokemon.pokemon_list", error='It was not possible to create a Battle')
            session['battle'] = Battle.from_dict(battle_dict)
            return render_template("pokemon_battle.html", colors=colors)
        else:
            return redirect(url_for("pokemon.pokemon_list"))
    elif request.method == 'POST':
        option = int(request.form.get('opcion'))
        if not session.get('battle'):
            return redirect(url_for("pokemon.pokemon_list"))
        winner,looser = battle_service.attack_battle(session.get('battle'), option)
        if winner and looser:
            # attacker_id,defender_id,attacker_pokemon,defender_pokemon,result
            attacker=session['trainer']
            attacker_id=attacker['id']
            defender=session['rival']
            defender_id=defender['id']
            attacker_pokemon=session['pokemon_selected']
            attacker_pokemon_id=attacker_pokemon['id']
            defender_pokemon=session['enemy_pokemon']
            defender_pokemon_id=defender_pokemon['id']
            
            result=battle_service.battle_result(winner.id,attacker_pokemon_id)
            

            create_battle_service(attacker_id=attacker_id,defender_id=defender_id,attacker_pokemon_id=attacker_pokemon_id,defender_pokemon_id=defender_pokemon_id,result=result)
             
            
            
            
            
            turnos = session['battle'].turno
            logHistoric = session['battle'].log
            session.pop('battle', None)
            session.pop('pokemon_selected', None)
            session.pop('my_pokemon_moves', None)
            session.pop('enemy_pokemon', None)
            session.pop('rival',None)
            return render_template("pokemon_winner.html", winner=winner, looser=looser, turnos=turnos, logList=logHistoric, colors=colors)

        else:
            return render_template("pokemon_battle.html", colors=colors)
