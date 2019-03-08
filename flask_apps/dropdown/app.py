# run with command: FLASK_APP=app.py; export FLASK_ENV=development; python -m flask run

from flask import Flask, request, render_template

import pandas as pd
import matplotlib
matplotlib.use('PS') 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# creates the app, and sets the static path
app = Flask(__name__, static_url_path='/static')

# this helps avoid caching images of plots
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# reads the data from the CSV
dat = pd.read_csv("cpu.csv")

# creates a select element, with an option for each numeric feature in the CSV
def build_options(feat=None):
    features = list(dat.columns.values)
    options = "<select form=\"form\", name=\"feat\">"
    for feature in features:
        if type(dat[feature][0]) is not str:
            if feature == feat:
                options += "<option value=\"" + feature + "\" selected>" + feature + "</option>"
            else:
                options += "<option value=\"" + feature + "\">" + feature + "</option>"
    options += "<select>"
    return options
    
# the function to run for the root URL
@app.route('/')
def on_load():
    
    # render the page
    html = render_template('initial.html', select=build_options())
    return html

# the function to run when the root URL gets a POST
@app.route('/', methods=['POST'])
def after_post():
    # gets the selected feature from post
    feat = request.form['feat']
    
    # create the plot
    image_path = 'static/plot.png'
    plt.hist(dat[feat])
    plt.title("Histogram of " + feat)
    plt.savefig(image_path)
    plt.close()
    
    # render the page
    html = render_template('main.html', select=build_options(feat))
    return html
    