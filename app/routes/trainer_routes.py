
from flask import Blueprint, render_template, request, session

from app.decorators import login_required
from app.services.battleDB_service import get_all_battles_details
from app.services.pokemon_service import get_pokemon_by_ID
from app.services.trainer_service import get_trainer_by_id_service


trainer_bp = Blueprint('trainer', __name__, template_folder='templates')

@trainer_bp.route("/", methods=["GET"])
@login_required
def trainer_details():

    id=session['trainer']['id']
    battles=get_all_battles_details(id)
    
    
    #     attacker_id,
    # defender_id,
    # attacker_pokemon_id,
    # defender_pokemon_id,
    # result):
    # 
    # 
    battles_details=[]
    if battles is not None:
        for battle in battles:
            battle_dict={}

            battle_dict['id']=battle.id

            battle_dict['result']='Win' if [battle.result]==True else 'Lose'
            if id==battle.attacker_id:
                battle_dict['rol']='Attacker'
                battle_dict['pokemon']=get_pokemon_by_ID(battle.attacker_pokemon)
            else:    
                battle_dict['rol']='Defender'
                battle_dict['pokemon']=get_pokemon_by_ID(battle.defender_pokemon)
            battles_details.append(battle_dict)

    
    # 
    # 
    
    
    return render_template("trainer_details.html", battles_details=battles_details)


#     for battle in battles:
        # battle_dict={}
        # battle_dict['id']=battle['id']
        # battle_dict['attacker']=get_trainer_by_id_service(battle['attacker_id'])
        # battle_dict['attacker']=get_trainer_by_id_service(battle['attacker_id'])
        # battle_dict['id']=battle['id']
        # battle_dict['id']=battle['id']
        # battle_dict['id']=battle['id']
        # battle_dict['id']=battle['id']
        # battle_dict['id']=battle['id']
        # battle_dict['id']=battle['id']
    # 
    # 
    # 
    
    
