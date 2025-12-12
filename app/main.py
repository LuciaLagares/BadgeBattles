import os
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import trainer
from app.routes.home_routes import home_bp
from app.routes.pokemon_routes import pokemon_bp
from app.routes.battle_routes import battle_bp
from app.routes.trainer_routes import trainer_bp
from app.database.db import db
import logging

from app.models.trainer import Trainer
from app.models.battleDB import BattleDB


from flask import Flask
from flask_session import Session

from app.services.trainer_service import add_opponets_service  # Importar la extensión

app = Flask(__name__, template_folder='templates')

# Configuración de Flask-Session
app.config["SESSION_TYPE"] = "filesystem"   # Guardar en ficheros
app.config["SESSION_PERMANENT"] = False     # Sesiones temporales
app.config["SESSION_FILE_DIR"] = "./.flask_session"  # Carpeta donde se guardan
app.secret_key = "clave_secreta"


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# y ponerlo abajo f"sqlite:///{BD_PATH}""
DB_PATH = os.path.join(BASE_DIR, "data", "trainer.db")


def sqlite_creator():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "creator": sqlite_creator
}


db.init_app(app)
# db=SQLAlchemy(app)

Session(app)


app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(pokemon_bp, url_prefix='/pokemons')
app.register_blueprint(battle_bp, url_prefix='/battle')
app.register_blueprint(trainer_bp, url_prefix='/trainer')


# Para ejecutar usar: ./.venv/Scripts/flask --app app.main create-tables
@app.cli.command("create-tables")
def create_tables():

    db.drop_all()
    db.create_all()
    print("Tables created.")


@app.cli.command("add-opponents")
def add_opponets():

    add_opponets_service()
    print('Opponents added succesfully')


logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug="True")
