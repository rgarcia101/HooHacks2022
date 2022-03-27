from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
PHOTO_FOLDER = os.path.join('static', 'photos')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['UPLOAD_FOLDER'] = PHOTO_FOLDER

db = SQLAlchemy(app)

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    hands_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'hands.png')
    return render_template('main.html', logo = full_filename, hands = hands_filename)

@app.route('/main.html')
def mainpage():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    hands_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'hands.png')
    return render_template('main.html', logo = full_filename, hands = hands_filename)

@app.route('/main_loggedin.html')
def loggedin():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    journal_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'journal.png')
    return render_template('main_loggedin.html', logo = full_filename, journal = journal_filename)

@app.route('/myjounral.html')
def journal():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('myjounral.html', logo = full_filename)

@app.route('/signup.html')
def signup():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    signup_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'singup.png')
    return render_template('signup.html', logo = full_filename, signup = signup_filename)

@app.route('/login.html')
def login():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    login_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'login.png')
    return render_template('login.html', logo = full_filename, login = login_filename)

@app.route('/resources.html')
def resources():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('resources.html', logo = full_filename)

if __name__ == "__main__":
    app.run(debug=True)