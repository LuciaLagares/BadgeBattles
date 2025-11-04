import datetime
from flask import Blueprint, current_app, jsonify, redirect, render_template, request, url_for

from app import colors
from app.services import pokemon_service

pokemon_bp = Blueprint('pokemon', __name__, template_folder='templates')

@pokemon_bp.route("/", methods=["GET", "POST"])
def pokemon_list():
    year = datetime.datetime.now().year
    pokemons = current_app.config["data"]
    trainer = request.args.get('trainer')
    gender = request.args.get('gender')
    error = ''


    if request.method == "POST":
        pokemon_finder = request.form.get('pokemon_finder')
        pokemon_found_id = None
        if (pokemon_finder is not None):
            for pokemon in pokemons:
                if pokemon['name'] == pokemon_finder.lower():
                    pokemon_found_id = pokemon['id']
                    break
            if pokemon_found_id is not None:

                return redirect(url_for('battle.pokemon_battle', year=year, pokemon_found_id=pokemon_found_id, trainer=trainer, gender=gender))
            else:
                error = 'Your pokemon is not in the list'
                return render_template("pokemon_list.html", year=year, pokemons=pokemons, colors=colors, trainer=trainer, error=error,gender=gender)
        else:
            return render_template("pokemon_list.html", year=year, pokemons=pokemons, colors=colors, trainer=trainer,gender=gender)
    else:
        return render_template("pokemon_list.html", year=year, pokemons=pokemons, colors=colors, trainer=trainer,error=error,gender=gender)


@pokemon_bp.route("/<int:pokemon_ID>/")
def pokemon_details(pokemon_ID):
    
    year = datetime.datetime.now().year
    visual_pokemon = pokemon_service.obtener_pokemon_por_ID(pokemon_ID)
    
    # Randomnizador de Shiny
    is_shiny = pokemon_service.is_pokemon_shiny(visual_pokemon.id, 10)

    return render_template("pokemon_details.html", year=year, pokemon=visual_pokemon, is_shiny=is_shiny, colors=colors)