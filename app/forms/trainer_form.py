

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Length


class TrainerForm(FlaskForm):
    trainer=StringField("Introduce el nombre del entrenador",validators=[
        DataRequired(message="El campo no puede estar vacio"),
        Length(min=3,max=15, message="El campo debe tener una longitud de entre 3 y 15")
    ])
    enviar=SubmitField("Enviar")
    