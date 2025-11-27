
import datetime
from flask import Blueprint, app, current_app, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session

from app.services.trainer_service import register_trainer

home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/', methods=['GET', 'POST'])
def welcome():
    year = datetime.datetime.now().year
    session["year"] = year
  
    if (request.method == 'POST'):
        session.clear()
        session["year"] = year
        name = request.form.get('trainer')
        gender = request.form.get('gender')
        password = request.form.get('password')
        error = False

        if (len(name) < 3):
            error = 'The trainer name needs to be longer than 3 letters'
        elif (len(name) > 15):
            error = 'The trainer name needs to be shorter than 15 letters'
        if error:
            return render_template('index.html', error=error)
        else:
            trainer=register_trainer(name, password, gender)
            # session['trainer'] = trainer.__dict__
            print(trainer.__dict__)
            

            return redirect(url_for('pokemon.pokemon_list'))
    elif (request.method == 'GET'):
        return render_template('index.html')

@home_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.welcome"))

@home_bp.route("/file")
def file_json():
    return jsonify(current_app.config["data"])

