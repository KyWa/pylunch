from app import app
from flask import render_template
from lunch import picker

@app.route('/')
@app.route('/index')
def index():
    choices = picker()
    return render_template('index.html', title="yeet", choices=choices)
