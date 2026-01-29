from math import ceil
from flask import Blueprint, abort, redirect, render_template, request, session, url_for
from app.colors import colors
from app.decorators import login_required
from app.services import battle_service, pokemon_service
from app.services.pokemon_service import calculate_page_pokemon, get_list_pokemons, get_pokemons


pokemon_bp = Blueprint('pokemon', __name__, template_folder='templates')


@pokemon_bp.route("/", methods=["GET", "POST"])
def pokemon_list():
    limit=8
    offset=0
    page=1
    total_pages=None
    page_str=request.args.get("page")
    if(page_str is not None):
        try:
            page=int(page_str)
            
            if page<=0:
                return redirect(url_for("pokemon.pokemon_list"))

            
            offset,limit=calculate_page_pokemon(page)
    
        except:
            
            return redirect(url_for("pokemon.pokemon_list",total_pages=total_pages, page=page))
   

    pokemons,pokemon_pages=get_list_pokemons(offset,limit)
 
    if len(pokemons)==0 and pokemon_pages is None:
        abort(404)
    error = ''
    
    if pokemons is None:
        pokemons=[]
    total_pages=ceil(pokemon_pages/8)
    if(page>total_pages):
        return redirect(url_for("pokemon.pokemon_list", page=total_pages))
    if request.method == "POST":
        pokemon_selected = request.form.get('pokemon_finder')       
        my_pokemon = pokemon_service.get_pokemon_by_name(
            pokemon_selected)
        if my_pokemon is not None:
            enemy_pokemon = battle_service.enemy_pokemon_selector(
                my_pokemon)
            enemy_pokemon=pokemon_service.get_pokemon_by_name(enemy_pokemon["name"])
            
           
            session['enemy_pokemon'] = enemy_pokemon.to_dict()
            trainer=session['trainer']
            trainer_id=trainer['id']
            rival = battle_service.rivalSpriteSelector(trainer_id)
            session['rival'] = rival.to_dict()
            my_pokemon_moves = battle_service.random_moves(
                my_pokemon, [])

            session['pokemon_selected'] = my_pokemon.to_dict()
            session['my_pokemon_moves'] = my_pokemon_moves

      
            return redirect(url_for('battle.pokemon_battle'))
        else:
            error = 'Your pokemon is not in the list'
            return render_template("pokemon_list.html", pokemons=pokemons, colors=colors, error=error,total_pages=total_pages, page=page)
    else: 
        return render_template("pokemon_list.html", pokemons=pokemons, colors=colors, error=error,total_pages=total_pages, page=page)


@pokemon_bp.route("/<int:pokemon_ID>/")
@login_required
def pokemon_details(pokemon_ID):


    visual_pokemon = pokemon_service.get_pokemon_by_ID(pokemon_ID)

    # Randomnizador de Shiny
    is_shiny = pokemon_service.is_pokemon_shiny(visual_pokemon.id, 10)

    return render_template("pokemon_details.html", pokemon=visual_pokemon, is_shiny=is_shiny, colors=colors)
