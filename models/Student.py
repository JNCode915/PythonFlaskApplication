

#from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

#import app


db = SQLAlchemy()
#db.init_app(app)
#@dataclass
class Student(db.Model):
   __tablename__ = 'Student'
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   school = db.Column(db.String(250))  
   

def __repr__(self):
   return f"Student(name='{self.name}', school='{self.school}')"

def __init__(self, name, school):
   self.name = name
   self.school = school