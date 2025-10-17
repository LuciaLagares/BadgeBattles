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
        error = False

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
    pokemon_finder = request.args.get('pokemon_finder')
    pokemon_found_id = None
    error = ''

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

    if (pokemon_finder is not None):
        for pokemon in pokemons:
            if pokemon['name'] == pokemon_finder.lower():
                pokemon_found_id = pokemon['id']
                break
        if pokemon_found_id is not None:
            # return render_template("pokemon_battle.html", year=year, my_pokemon=pokemon_found, enemy_pokemon=enemy_pokemon, trainer=trainer, colors=colors)
            return redirect(url_for('pokemon_battle', year=year, pokemon_found_id=pokemon_found_id, trainer=trainer))
        else:
            error = 'Your pokemon is not in the list'
            return render_template("pokemon_list.html", year=year, pokemons=pokemons, colors=colors, trainer=trainer, error=error)
    else:
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


@app.route("/pokemon_battle/")
def pokemon_battle():
    #  year=year, my_pokemon=pokemon_found, trainer=trainer, colors=colors
    pokemons = app.config["data"]
    year = request.args.get('year')
    my_pokemon_id = request.args.get('pokemon_found_id')
    trainer = request.args.get('trainer')
    enemy_pokemon = None
    my_pokemon = None

    # Rival Dict
    rivals = [
        {
            'name': 'Iker Jimenez',
            'sprite': url_for('static', filename='images/rival_sprite/Iker.webp'),
        },
        {
            'name':'Cristiano Ronaldo', 
            'sprite': url_for('static', filename='images/rival_sprite/Cristiano.webp'), 
        },
        {
            'name':'Santiago Abascal', 
            'sprite':url_for('static', filename='images/rival_sprite/Abascal.webp'),
        },
        {
            'name':'Estudiante DAW',
             'sprite':url_for('static', filename='images/rival_sprite/Estudiante.webp'),
        },
        {
            'name':'Felipe VI', 
            'sprite':url_for('static', filename='images/rival_sprite/Felipe_VI.webp'),},
        {
            'name':'Francisco Franco', 
            'sprite':url_for('static', filename='images/rival_sprite/Franco.webp'),
        },
        {
            'name':'Guiri', 
            'sprite':url_for('static', filename='images/rival_sprite/Guiri.webp'),
        },
        {
            'name':'Ignatius', 
            'sprite':url_for('static', filename='images/rival_sprite/Ignatius.webp'),
        },
        {
            'name':'C++ Programmer', 
            'sprite':url_for('static', filename='images/rival_sprite/Programador.webp'),
        },
        {
            'name':'Pedro Sanchez', 
            'sprite':url_for('static', filename='images/rival_sprite/Pedro_Sanchez.webp'),
        },
        {
            'name':'Mariano Rajoy', 
            'sprite':url_for('static', filename='images/rival_sprite/Rajoy.webp'),
        },
        {
            'name':'Pérez Reverte', 
            'sprite':url_for('static', filename='images/rival_sprite/Reverte.webp'),
        }
    ]
        

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
    #
    for pokemon in pokemons:
        if str(pokemon['id']) == my_pokemon_id:
            my_pokemon = pokemon
            break

    def enemyPokemonSelector():
        randomPokemonNumber = random.randint(0, len(pokemons)-1)
        enemy_pokemon = pokemons[randomPokemonNumber]
        if len(pokemons) >= 2:
            if (enemy_pokemon['id'] == my_pokemon['id']):
                return enemyPokemonSelector()
        return enemy_pokemon

    def rivalSpriteSelector():
        return rivals[random.randint(0, len(rivals)-1)]

    enemy_pokemon = enemyPokemonSelector()
    rival = rivalSpriteSelector()

    return render_template("pokemon_battle.html", year=year, my_pokemon=my_pokemon, enemy_pokemon=enemy_pokemon, trainer=trainer, colors=colors, rival=rival)


if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug="True")
