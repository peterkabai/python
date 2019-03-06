# run with command: FLASK_APP=app.py; flask run

from flask import Flask, request, render_template

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

dat = pd.read_csv("cpu.csv")

def build_options(features, feat=None):
    options = "<select form=\"form\", name=\"feat\">"
    for feature in features:
        if type(dat[feature][0]) is not str:
            if feature == feat:
                options += "<option value=\"" + feature + "\" selected>" + feature + "</option>"
            else:
                options += "<option value=\"" + feature + "\">" + feature + "</option>"
    options += "<select>"
    return options
    
@app.route('/')
def on_load():
    
    # get all column names
    features = list(dat.columns.values)
    options = build_options(features)
        
    # render the page
    html = render_template('initial.html', select=options)
    return html

@app.route('/', methods=['POST'])
def after_post():
    feat = request.form['feat']
    features = list(dat.columns.values)
    options = build_options(features, feat)
    
    # create the plot
    plt.figure(1)
    image_path = 'static/plot.png'
    plt.hist(dat[feat])
    plt.title("Histogram of " + feat)
    plt.savefig(image_path)
    plt.close()
    
    html = render_template('main.html', select=options)
    return html