# run with command: FLASK_APP=app.py; export FLASK_ENV=development; python -m flask run

from flask import Flask, request, render_template

import pandas as pd
import matplotlib
matplotlib.use('PS') 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# reads the data from the CSV
dat = pd.read_csv("crash_small.csv")

def get_unique_months(column):
    year_month = []
    for date in np.array(column):
        year_month.append(date[6:10] + "-" + date[0:2])
    months = list(set(year_month))
    months.sort()
    return months
    
def get_unique(column):
    print ("ok")
    c = []
    for i in np.array(column):
        if i is not None:
            c.append(i)
    uniq = list(set(c))
    print ("ok1")
    #uniq.sort()
    return uniq

def clean_up_date(column):
    year_month = []
    for date in np.array(column):
        year_month.append(date[6:10] + "-" + date[0:2])
    return(year_month)
    
months = get_unique_months(dat["Crash Date/Time"])
dat["year_month"] = clean_up_date(dat["Crash Date/Time"])

def join_to_arr_string(arr):
    to_return = "["
    num_val = len(arr)
    i = 0
    while i < num_val:
        to_return += "\"" + str(arr[i]) + "\""
        if i < num_val-1:
            to_return += ","
        i += 1
    to_return += "]"
    return(to_return) 

# build typeahead multi select in javascript
def typeahead(labels):
    return ""
       
# creates the app, and sets the static path
app = Flask(__name__, static_url_path='/static')

# this helps avoid caching images of plots
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# the function to run for the root URL
@app.route('/')
def on_load():
    
    # render the page
    roads = get_unique(dat["Road Name"])
    html = render_template('initial.html', control=typeahead(roads))
    return html

# the function to run when the root URL gets a POST
@app.route('/', methods=['POST'])
def after_post():
    
    # gets the selected feature from post
    slide = request.form['slide'].split(" to ")
    bottom = slide[0]
    top = slide[1]
    print(bottom)
    print(top)
    
    # create the plot
    image_path = 'static/plot.png'
    plt.figure(1)
    mask = (dat["year_month"] >= bottom) & (dat["year_month"] <= top)
    dat.loc[mask, "year_month"].value_counts().sort_index().plot(kind="bar", color="red")
    plt.title("Crashes Per Month")
    plt.grid(color='gray', linestyle='-', linewidth=1)
    
    plt.savefig(image_path, bbox_inches='tight')
    plt.close()
    
    # render the page
    html = render_template('main.html', slider=slider(min_val, max_val, months.index(bottom), months.index(top), months))
    return html
    