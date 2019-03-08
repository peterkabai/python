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

def clean_up_date(column):
    year_month = []
    for date in np.array(column):
        year_month.append(date[6:10] + "-" + date[0:2])
    return(year_month)
    
months = get_unique_months(dat["Crash Date/Time"])
dat["year_month"] = clean_up_date(dat["Crash Date/Time"])

# sets initial range and initial values
min_val = 0
max_val = int(len(months)-1)
low = min_val
high = max_val

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
        

# builds slider javascript
def slider(min_val, max_val, low, high, labels):
    return "$( function() { \
      var lab = " + join_to_arr_string(labels) + "; \
      $( '#slider-range' ).slider({ \
        range: true, \
        min: " + str(min_val) + ", \
        max: " + str(max_val) + ", \
        values: [ " + str(low) + ", " + str(high) + " ], \
        slide: function( event, ui) { \
          $( '#amount' ).val(lab[ui.values[ 0 ]] + ' to ' + lab[ui.values[ 1 ]] ); \
        } \
      }); \
      $( '#amount' ).val( lab[" + str(low) + "] + ' to ' + lab[" + str(high) + "] ); \
    } );"
       
# creates the app, and sets the static path
app = Flask(__name__, static_url_path='/static')

# this helps avoid caching images of plots
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# the function to run for the root URL
@app.route('/')
def on_load():
    
    # render the page
    html = render_template('initial.html', slider=slider(min_val, max_val, low, high, months))
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
    