
import datetime
from flask import Blueprint, app, current_app, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session

from app.models.exceptions import TrainerAlreadyExistException, TrainerNotFound, WrongPassword
from app.services.trainer_service import authenticate_trainer, register_trainer

home_bp = Blueprint('home', __name__, template_folder='templates')


@home_bp.route('/', methods=['GET', 'POST'])
def welcome():
    year = datetime.datetime.now().year
    session["year"] = year

    if (request.method == 'POST'):
        session.clear()
        session["year"] = year
        name = request.form.get('trainer')
        password = request.form.get('password')
        error = False

        if  name is None:
            error = 'The trainer name is a required field'
        elif password is None:
            error = 'Password is a required field.'
        if error:
            return render_template('index.html', error=error)
        else:
            try:
                trainer = authenticate_trainer(name, password)
                session['trainer'] = trainer.to_dict()
            
            except TrainerNotFound:
                error="Trainer name not found in the DataBase"
                return render_template('index.html', error=error)
            except WrongPassword:
                error="Wrong password for that user name"
                return render_template('index.html', error=error)
            return redirect(url_for('pokemon.pokemon_list'))
    elif (request.method == 'GET'):
        return render_template('index.html')


@home_bp.route("/register", methods=["GET","POST"])
def register():
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
            error = 'The trainer name needs to be longer than 3 letters.'
        elif (len(name) > 15):
            error = 'The trainer name needs to be shorter than 15 letters.'
        elif(len(password) < 4):
            error = 'The password needs to be longer than 4 letters'
        elif not password:
            error='Password is a required field.'
        elif not gender:
            error='You must introduce your gender.'
        if error:
            return render_template('register.html', error=error)
        else:
            try:

                trainer = register_trainer(name, password, gender)
                session['trainer'] = trainer.to_dict()
                return redirect(url_for('pokemon.pokemon_list'))
            except TrainerAlreadyExistException:
                    error="Trainer name already exist on the DataBase"
                    return render_template('register.html', error=error)
                
    elif (request.method == 'GET'):
        return render_template('register.html')

@home_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.welcome"))


@home_bp.route("/file")
def file_json():
    return jsonify(current_app.config["data"])
