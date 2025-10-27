
import datetime
from flask import Blueprint, current_app, jsonify, redirect, render_template, request, url_for

home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/', methods=['GET', 'POST'])
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
            return redirect(url_for('pokemon.pokemon_list', trainer=trainer, gender=gender))
    elif (request.method == 'GET'):
        return render_template('index.html', year=year)
    
@home_bp.route("/file")
def file_json():
    return jsonify(current_app.config["data"])
# @app.route('/bienvenida')
# def hello_welcome():
#     year=datetime.datetime.now().year
#     return render_template('index.html', year=year)