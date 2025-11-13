
import datetime
from flask import Blueprint, app, current_app, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session

home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/', methods=['GET', 'POST'])
def welcome():
    year = datetime.datetime.now().year
    session["year"] = year
    if (request.method == 'POST'):
        trainer = request.form['trainer']
        gender = request.form['gender']
        error = False

        if (len(trainer) < 3):
            error = 'The trainer name needs to be longer than 3 letters'
        elif (len(trainer) > 15):
            error = 'The trainer name needs to be shorter than 15 letters'
        if error:
            return render_template('index.html', error=error)
        else:
            session['trainer'] = trainer
            session['gender'] = gender
            return redirect(url_for('pokemon.pokemon_list'))
    elif (request.method == 'GET'):
        return render_template('index.html')
    
@home_bp.route("/file")
def file_json():
    return jsonify(current_app.config["data"])

