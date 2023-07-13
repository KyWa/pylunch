from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    choices = lunch()
    return render_template('index.html', title="yeet", choices=choices)
