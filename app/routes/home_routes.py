
import datetime
from flask import Blueprint, current_app, jsonify, redirect, render_template, request, url_for
from app.forms.trainer_form import TrainerForm

home_bp=Blueprint('home',__name__,template_folder='templates')

@home_bp.route('/', methods=['GET', 'POST'])
def welcome():
    form=TrainerForm() #Se instancia de la clase
    
    year = datetime.datetime.now().year
    
    if form.validate_on_submit():
        #Ya no harian falta las validaciones porque estan en el formulario
        trainer =form.trainer.data
        # gender = request.form['gender']
        return trainer
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
        return render_template('index.html', form=form, year=year)
    
    
# @home_bp.route("/file")
# def file_json():
#     return jsonify(current_app.config["data"])