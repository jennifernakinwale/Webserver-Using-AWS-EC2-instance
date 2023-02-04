# -*- coding: utf-8 -*-
  
import csv
import sqlite3

from collections import Counter

from flask import *
from flask_login import LoginManager, login_required, logout_user, login_user #handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time

app = Flask(__name__)
app.config.from_object(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


DATABASE = '/var/www/html/flaskapp/user.db'

conn = sqlite3.connect('/var/www/html/flaskapp/user.db')
cur = conn.cursor()

#user_loader needed for flask_login to work
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def connect_to_database():
    return sqlite3.connect(app.config['DATABASE'])


def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def execute_query(query, args=()):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

#landing page
@app.route('/homepage')
def my_form():
    return render_template('homepage.html')


#registration page
@app.route('/registerpage.html')
def my_form2():
    return render_template('registerpage.html')

@app.route('/registerpage.html', methods=['POST'])
def registration_submit():
    #return "registration complete"
    conn = sqlite3.connect('/var/www/html/flaskapp/user.db')
    cur = conn.cursor()
    Firstname = request.form['Firstname']
    #return request.form['Firstname']
    Lastname = request.form['Lastname']
    #return request.form['Lastname']
