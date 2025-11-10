import datetime
import json
from pathlib import Path
from flask import Blueprint, app, current_app, jsonify, redirect, render_template, request, session, url_for

from app.colors import colors
from app.services import pokemon_service
from app.services.pokemon_service import listar_pokemons


pokemon_bp = Blueprint('pokemon', __name__, template_folder='templates')


@pokemon_bp.route("/", methods=["GET", "POST"])
def pokemon_list():
    pokemons = listar_pokemons()
    error = ''

    if request.method == "POST":
        pokemon_selected = request.form.get('pokemon_finder')
        session['pokemon_selected'] = pokemon_service.obtener_pokemon_por_nombre(pokemon_selected)
        if session['pokemon_selected'] is not None:
            return redirect(url_for('battle.pokemon_battle'))  
        else:
            error = 'Your pokemon is not in the list'
            return render_template("pokemon_list.html", pokemons=pokemons, colors=colors,error=error)
    else:
        return render_template("pokemon_list.html", pokemons=pokemons, colors=colors, error=error)


@pokemon_bp.route("/<int:pokemon_ID>/")
def pokemon_details(pokemon_ID):

    year = datetime.datetime.now().year
    visual_pokemon = pokemon_service.obtener_pokemon_por_ID(pokemon_ID)

    # Randomnizador de Shiny
    is_shiny = pokemon_service.is_pokemon_shiny(visual_pokemon.id, 10)
    return render_template("pokemon_details.html", pokemon=visual_pokemon, is_shiny=is_shiny, colors=colors)
