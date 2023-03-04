from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from datetime import timezone, datetime

db = SQLAlchemy()



def load_user(id):
    return User.query.get(int(id))


user_comp = db.Table(
    "user_comp",
    db.Column('user_id', db.Integer, db.ForeignKey('User.id'), nullable=False),
    db.Column('demon_id', db.Integer, db.ForeignKey('Demon.demon_id'), nullable=False)
)

demons_skills = db.Table(
    "demons_skills",
    db.Column('skill_id', db.Integer, db.ForeignKey('Skill.skill_id'), nullable=False),
    db.Column('demon_id', db.Integer, db.ForeignKey('Demon.demon_id'), nullable=False)
)



class User(db.Model, UserMixin):
    __tablename__ = "User" 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    demon = db.relationship("Demon", 
        secondary = user_comp, 
        backref= "user_comp", lazy="dynamic")
    
    def __init__(self, username,  email, password):
        self.username = username
        self.email = email
        self.password = password

    

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def catch_demon(self, caught_demon):
        self.demon.append(caught_demon)
        db.session.commit()

class Skill(db.Model):
    __tablename__ = "Skill"
    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(60), nullable=False, unique=True)
    Type = db.Column(db.String(50), nullable=False, unique=True)
    Affinity = db.Column(db.String(50), nullable=False)
    Power = db.Column(db.Integer, nullable=False)
    Range = db.Column(db.String(50), nullable=False)
    


    def __init__(self, skill_name, Type, Affinity, Power, Range):
        self.skill_name = skill_name
        self.Type = Type
        self.Affinity = Affinity
        self.Power = Power
        self.Range = Range

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()


class Demon(db.Model):
    __tablename__ ="Demon"
    demon_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    Image = db.Column(db.String(200), nullable=False)
    HP = db.Column(db.Integer, nullable=False)
    Strength = db.Column(db.Integer, nullable=False)
    Magic = db.Column(db.Integer, nullable=False)
    Defense = db.Column(db.Integer, nullable=False)
    Weak = db.Column(db.String(50), nullable=False)
    Null = db.Column(db.String(50), nullable=False)
    Repel = db.Column(db.String(50), nullable=False)
    Lore = db.Column(db.String(1000), nullable=False)
    skills = db.relationship("Skill", 
        secondary = demons_skills, 
        backref= "demons_skills", lazy="dynamic")



    def __init__(self, name, Image, HP, Strength, Magic, Defense, Weak, Null, Repel, Lore):
        self.name = name
        self.Image = Image
        self.HP = HP
        self.Strength = Strength
        self.Magic = Magic
        self.Defense = Defense
        self.Weak = Weak
        self.Null = Null
        self.Repel = Repel
        self.Lore = Lore

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    

    

