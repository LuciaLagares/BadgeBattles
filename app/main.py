import math
import random
from flask import Flask, current_app, json, jsonify, render_template, request, redirect, url_for
import datetime

from colors import colors 

import services.pokemon_service as pokemon_service
import services.battle_service as battle_service

app = Flask(__name__, template_folder='templates')

with open("./data/data.json", encoding="utf-8") as fichero_data:
    app.config["data"] = json.load(fichero_data)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    year = datetime.datetime.now().year
    if (request.method == 'POST'):
        trainer = request.form['trainer']
        gender = request.form['gender']
        error = False

        if (len(trainer) < 3):
            error = 'The trainer name needs to be longer than 3 letters'
        elif (len(trainer) > 15):
            error = 'The trainer name needs to be shorter than 15 letters'
        if error:
            return render_template('index.html', year=year, error=error)
        else:
            return redirect(url_for('pokemon_list', trainer=trainer, gender=gender))
    elif (request.method == 'GET'):
        return render_template('index.html', year=year)


@app.route("/file")
def file_json():
    return jsonify(current_app.config["data"])
# @app.route('/bienvenida')
# def hello_welcome():
#     year=datetime.datetime.now().year
#     return render_template('index.html', year=year)


@app.route("/pokemons/", methods=["GET", "POST"])
def pokemon_list():
    year = datetime.datetime.now().year
    pokemons = app.config["data"]
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

                return redirect(url_for('pokemon_battle', year=year, pokemon_found_id=pokemon_found_id, trainer=trainer, gender=gender))
            else:
                error = 'Your pokemon is not in the list'
                return render_template("pokemon_list.html", year=year, pokemons=pokemons, colors=colors, trainer=trainer, error=error,gender=gender)
        else:
            return render_template("pokemon_list.html", year=year, pokemons=pokemons, colors=colors, trainer=trainer,gender=gender)
    else:
        return render_template("pokemon_list.html", year=year, pokemons=pokemons, colors=colors, trainer=trainer,error=error,gender=gender)


@app.route("/pokemons/<int:pokemon_ID>/")
def pokemon_details(pokemon_ID):
    
    year = datetime.datetime.now().year
    visual_pokemon = pokemon_service.obtener_pokemon_por_ID(pokemon_ID)
    
    # Randomnizador de Shiny
    is_shiny = pokemon_service.is_pokemon_shiny(visual_pokemon.id, 10)

    return render_template("pokemon_details.html", year=year, pokemon=visual_pokemon, is_shiny=is_shiny, colors=colors)


@app.route("/pokemon_battle/")
def pokemon_battle():
    #  year=year, my_pokemon=pokemon_found, trainer=trainer, colors=colors
    year = request.args.get('year')
    my_pokemon_id = int(request.args.get('pokemon_found_id'))
    trainer = request.args.get('trainer')
    gender = request.args.get('gender')
    enemy_pokemon = None
    my_pokemon = pokemon_service.obtener_pokemon_por_ID(my_pokemon_id)

    random_moves = battle_service.random_moves(my_pokemon, [])

    enemy_pokemon = battle_service.enemyPokemonSelector(my_pokemon)


    def rivalSpriteSelector():
         # Rival Dict
        from rivals import rivals
        return rivals[random.randint(0, len(rivals)-1)]

    
    rival = rivalSpriteSelector()
  

    return render_template("pokemon_battle.html", year=year, my_pokemon=my_pokemon, enemy_pokemon=enemy_pokemon, trainer=trainer, colors=colors, rival=rival, gender=gender, moves=random_moves)


if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug="True")
