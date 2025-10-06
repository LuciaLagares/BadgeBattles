from flask import Flask, current_app, json, jsonify, render_template; 
import datetime 

app = Flask(__name__, template_folder='templates')

with open("./data/data.json", encoding="utf-8") as fichero_data:
    app.config["data"]=json.load(fichero_data)

@app.route('/')
# def hello_world():
#     return 'Hello, World!'
def welcome():
    year=datetime.datetime.now().year
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
    year=datetime.datetime.now().year
    pokemons = app.config["data"]
    return render_template("pokemon_list.html", year=year,pokemons=pokemons)

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug="True")