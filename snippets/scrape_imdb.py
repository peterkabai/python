# This downloads the genre, title, rating, year and description 
# of 60,000 IMDB titles. 100 pages of results, with 50 on each page, for 
# 12 different genres. It takes about 28 minutes to run, and saves a CSV file.

import urllib.request
import re
from string import printable

def get_page(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    request = urllib.request.Request(url, headers = {'User-Agent': user_agent})
    page = urllib.request.urlopen(request).read().decode('utf-8')
    return(page)
    
def get_title_info(title_block):
    
    # Get the description
    try:
        description = title_block.split("<p class=\"text-muted\">")[1].split("</p>")[0]
        description = re.sub("\n", "", description)
        description = re.sub("  ", "", description)
        description = re.sub("\"", "\'", description)
        if len(description.split("<a href")) != 1: description = ""
    except IndexError:
        description = ""
    
    # Get the rating
    try:
        rating = title_block.split("<strong>")[1].split("</strong>")[0]
    except IndexError:
        rating = ""
        
    # Get the year
    try:
        year = title_block.split("text-muted unbold\">(")[1].split("</")[0]
        year = re.sub("\\)", "", year)
        year = re.sub("\\(", "", year)
        year = re.sub("I", "", year)
        year = re.sub(" ", "", year)
        year = re.sub("TVMovie", "", year)
    except IndexError:
        year = ""
        
    # Get the title
    try:
        title = title_block.split("adv_li_tt\"\n>")[1].split("</a")[0]
    except IndexError:
        title = ""
        
    return(title, rating, year, description)
    
genres = [
    'comedy',
    'sci-fi',
    'horror',
    'romance',
    'action',
    'thriller',
    'drama',
    'mystery',
    'crime',
    'animation',
    'adventure',
    'fantasy'
]
    
pages_per_genre = 100
lines = 0
csv = open("../data/imdb.csv", "w+")
csv.write("genre,title,rating,year,description\r\n")

for genre in genres:
    for page_num in range(pages_per_genre):
        start = page_num * 50 + 1
        page = get_page("https://www.imdb.com/search/title?genres=" + genre + "&start=" + str(start))  
        elements = page.split("<div class=\"lister-item-content\">")[1:]
        for element in elements:
            title, rating, year, description = get_title_info(element)
            
            csv.write("\"" + genre + "\",\"" + title + "\",\"" + rating + "\",\"" + year + "\",\"" + description + "\"\r\n")
            lines += 1
            print(str(lines) + " rows saved", end="\r")
            
csv.close() 
print(str(lines) + " rows saved")
