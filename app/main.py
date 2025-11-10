
from flask import Flask


from app.routes.home_routes import home_bp
from app.routes.pokemon_routes import pokemon_bp
from app.routes.battle_routes import battle_bp
from app.colors import colors 
import logging

import app.services.pokemon_service as pokemon_service
import app.services.battle_service as battle_service

from flask import Flask, session
from flask_session import Session  # Importar la extensión

app = Flask(__name__, template_folder='templates')

# Configuración de Flask-Session
app.config["SESSION_TYPE"] = "filesystem"   # Guardar en ficheros
app.config["SESSION_PERMANENT"] = False     # Sesiones temporales
app.config["SESSION_FILE_DIR"] = "./.flask_session"  # Carpeta donde se guardan
app.secret_key = "clave_secreta"

# Inicializar la extensión
Session(app)



app.register_blueprint(home_bp, url_prefix = '/')
app.register_blueprint(pokemon_bp, url_prefix = '/pokemons')
app.register_blueprint(battle_bp, url_prefix = '/battle')

logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug="True")
