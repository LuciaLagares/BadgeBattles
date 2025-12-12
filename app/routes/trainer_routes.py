
from flask import Blueprint, render_template


trainer_bp = Blueprint('trainer', __name__, template_folder='templates')

@trainer_bp.route("/", methods=["GET"])
def trainer_details():
    return render_template("trainer_details.html")
    
    
