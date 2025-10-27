import math
import random
from flask import Flask, current_app, json, jsonify, render_template, request, redirect, url_for
import datetime
from app.routes.home_routes import home_bp
from app.routes.pokemon_routes import pokemon_bp
from app.routes.pokemon_battle_routes import battle_bp
from app.colors import colors 

import app.services.pokemon_service as pokemon_service
import app.services.battle_service as battle_service

app = Flask(__name__, template_folder='templates')

#Definir blueprints. Registrarlos

app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(pokemon_bp, url_prefix='/pokemons')
app.register_blueprint(battle_bp, url_prefix='/')

app.secret_key = "BadgeBattles"



# @app.route('/bienvenida')
# def hello_welcome():
#     year=datetime.datetime.now().year
#     return render_template('index.html', year=year)







if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug="True")
