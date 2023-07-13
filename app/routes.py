from app import app
from flask import render_template
import lunch

@app.route('/')
@app.route('/index')
def index():
    choices = picker()
    return render_template('index.html', title="yeet", choices=choices)
