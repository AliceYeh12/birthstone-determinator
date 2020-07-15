# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=["GET", "POST"])
def results():
    if request.method == "POST":
        info = model.get_gemstone(request.form['birthdate'])
        props = {
            'name': request.form['name'],
            'gemstone': info['stone'],
            'img': info['img'],
            'desc': info['desc']
        }
        return render_template('results.html', props=props)
    else:
        return "Error"