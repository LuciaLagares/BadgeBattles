import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.home_routes import home_bp
from app.routes.pokemon_routes import pokemon_bp
from app.routes.battle_routes import battle_bp
from app.database.db import db
import logging



from flask import Flask
from flask_session import Session  # Importar la extensión

app = Flask(__name__, template_folder='templates')

# Configuración de Flask-Session
app.config["SESSION_TYPE"] = "filesystem"   # Guardar en ficheros
app.config["SESSION_PERMANENT"] = False     # Sesiones temporales
app.config["SESSION_FILE_DIR"] = "./.flask_session"  # Carpeta donde se guardan
app.secret_key = "clave_secreta"


BASE_DIR=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
BD_PATH=os.path.join(BASE_DIR,"data","trainer.db") #y ponerlo abajo f"sqlite:///{BD_PATH}""
app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{BD_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
# db=SQLAlchemy(app) 

Session(app)



app.register_blueprint(home_bp, url_prefix = '/')
app.register_blueprint(pokemon_bp, url_prefix = '/pokemons')
app.register_blueprint(battle_bp, url_prefix = '/battle')


@app.cli.command("create-tables") #Para ejecutar usar: ./.venv/Scripts/flask --app app.main create-tables
def create_tables():
    db.drop_all()
    
    db.create_all()
    print("Tables created.")

logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug="True")
