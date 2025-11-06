import datetime
import json
from pathlib import Path
from flask import Blueprint, app, current_app, jsonify, redirect, render_template, request, url_for

from app import colors
from app.services import pokemon_service
from app.services.pokemon_service import listar_pokemons
from app.services.pokemon_service import obtener_pokemon_por_nombre

pokemon_bp = Blueprint('pokemon', __name__, template_folder='templates')


@pokemon_bp.route("/", methods=["GET", "POST"])
def pokemon_list():
    year = datetime.datetime.now().year
    pokemons = listar_pokemons()
    trainer = request.args.get('trainer')
    gender = request.args.get('gender')
    error = ''

    if request.method == "POST":
        pokemon_name = request.form.get('pokemon_finder')
        

        
        if pokemon_name is not None:
            return redirect(url_for('battle.pokemon_battle', year=year, pokemon=pokemon_name, trainer=trainer, gender=gender))  
        else:
            error = 'Your pokemon is not in the list'
            return render_template("pokemon_list.html", year=year, pokemons=pokemons, colors=colors, trainer=trainer, error=error, gender=gender)
    else:
        return render_template("pokemon_list.html", year=year, pokemons=pokemons, colors=colors, trainer=trainer, error=error,gender=gender)


@pokemon_bp.route("/<int:pokemon_ID>/")
def pokemon_details(pokemon_ID):

    year = datetime.datetime.now().year
    visual_pokemon = pokemon_service.obtener_pokemon_por_ID(pokemon_ID)

    # Randomnizador de Shiny
    is_shiny = pokemon_service.is_pokemon_shiny(visual_pokemon.id, 10)

    return render_template("pokemon_details.html", year=year, pokemon=visual_pokemon, is_shiny=is_shiny, colors=colors)
