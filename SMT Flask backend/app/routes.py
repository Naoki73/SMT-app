import requests as r
from app import app
# from app.services import findpokemon
from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required, login_user, logout_user

from .models import Demon, User, user_comp, demons_skills
import json

from .test import demondata, skilldata


#If I get the absolute index length of how long Demons is, import random package, then I can use random to choose a random number in the length of Demons 

#make sure we're calling to one demon, figure out logic to go in between the 2 applications and what they'll be able to access
#
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/demons')
def demons():
    return demondata

@app.route('/skills')
def skilldata():
    return skilldata 

if __name__ == '__main__':
    app.run(debug=True)





