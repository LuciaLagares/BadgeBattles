from app.database import db


class TrainerDB(db.Model):
    __tablename__ = "TrainerDB"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(100), nullable = False)