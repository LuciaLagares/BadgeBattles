from sqlalchemy import Column, Integer, String
from app.database.db import db
class Trainer(db.Model):
    __tablename__ = "TrainerDB"
    
    id = Column(Integer, autoincrement=True,primary_key = True)
    name = Column(String(100), nullable = False, unique = True)
    gender = Column(String(100), nullable = False)
    password = Column(String(100), nullable = False)
    

    def __init__(self, name, password,gender):
        self.name = name
        self.password = password
        self.gender = gender


    
