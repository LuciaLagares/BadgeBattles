import math
import random
from flask import Flask, current_app, json, jsonify, render_template, request, redirect, url_for
import datetime

app = Flask(__name__, template_folder='templates')

with open("./data/data.json", encoding="utf-8") as fichero_data:
    app.config["data"] = json.load(fichero_data)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    pokemons = app.config["data"]
    year = datetime.datetime.now().year
    if (request.method == 'POST'):
        trainer = request.form['trainer']
        error=False
        
        if (len(trainer) < 3):
            error = 'The trainer name needs to be longer than 3 letters'
        elif (len(trainer) > 15):
            error = 'The trainer name needs to be shorter than 15 letters'
        if error:
            return render_template('index.html', year=year, error=error)
        else:
            return redirect(url_for('pokemon_list', trainer=trainer))
    elif (request.method == 'GET'):
        return render_template('index.html', year=year)


@app.route("/file")
def file_json():
    return jsonify(current_app.config["data"])
# @app.route('/bienvenida')
# def hello_welcome():
#     year=datetime.datetime.now().year
#     return render_template('index.html', year=year)


@app.route("/pokemons/")
def pokemon_list():
    year = datetime.datetime.now().year
    pokemons = app.config["data"]
    trainer = request.args.get('trainer')
    colors = {
        'electric': 'yellow',
        'fire': 'red',
        'flying': 'lightskyblue',
        'grass': 'olive',
        'poison': 'fuchsia',
        'water': 'blue',
        'fighting': 'saddlebrown',
        'dragon': 'mediumblue',
        'normal': 'bisque',
        'ground': 'tan',
        'dark': 'darkslategrey',
        'steel': 'lightslategray',
        'fairy': 'violet',
        'ice': 'lightsteelblue'
    }

    return render_template("pokemon_list.html", year=year, pokemons=pokemons, colors=colors, trainer=trainer)


@app.route("/pokemons/<int:pokemon_ID>/")
def pokemon_details(pokemon_ID):
    year = datetime.datetime.now().year
    visual_pokemon = None

    pokemons = app.config["data"]
    for pokemon in pokemons:
        if pokemon['id'] == pokemon_ID:
            visual_pokemon = pokemon

            # Randomnizador de Shiny
    def is_pokemon_shiny(id, max):

        shiny = int(random.randint(0, max))
        while (id > max):
            id = math.trunc(math.sqrt(id))
        if id == shiny:
            return True
        else:
            return False
    is_shiny = is_pokemon_shiny(visual_pokemon['id'], 10)

    colors = {
        'electric': 'yellow',
        'fire': 'red',
        'flying': 'lightskyblue',
        'grass': 'olive',
        'poison': 'fuchsia',
        'water': 'blue',
        'fighting': 'saddlebrown',
        'dragon': 'mediumblue',
        'normal': 'bisque',
        'ground': 'tan',
        'dark': 'darkslategrey',
        'steel': 'lightslategray',
        'fairy': 'violet',
        'ice': 'lightsteelblue'
    }

    return render_template("pokemon_details.html", year=year, pokemon=visual_pokemon, is_shiny=is_shiny, colors=colors)


if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug="True")
