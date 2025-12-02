from sqlalchemy import Column, Integer, String
from app.database.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import relationship
class Trainer(db.Model):
    __tablename__ = "TrainerDB"
    
    id = Column(Integer, autoincrement=True,primary_key = True)
    name = Column(String(100), nullable = False, unique = True)
    gender = Column(String(100), nullable = False)
    password_hashed = Column(String(255), nullable = False)
    
    battles=relationship("Battle",back_populates='trainers')
    

    def __init__(self, name, password,gender):
        self.name = name
        self.password_hashed = generate_password_hash(password)
        self.gender = gender
    
    def check_password(self, password):
        return check_password_hash(self.password_hashed, password)
    
    def to_dict(self):
        trainer={
            "id":self.id,
            "name":self.name,
            "gender":self.gender,  
        }
        return trainer
    

    
    

    
