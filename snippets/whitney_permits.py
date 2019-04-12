import calendar
import os
import set_environ
import re
import sys
import time
import send_email as gmail
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def get_element(browser, name, elem_type="id", index="first", tries=0, sleep_time=0.25, try_for=5):

    # If this is the first try to get the element, wait a bit
    if tries == 0:
        time.sleep(sleep_time)

    # If it's taken longer than try_for time, then print an error and exit
    if tries * sleep_time > try_for:
        print ("ERROR: getting '" + name + "' took longer than " + str(try_for) + " seconds.")
        exit()

    # Get the element by name and element type
    try:
        if elem_type == "id":
            if index == "all":
                element = browser.find_elements_by_id(name)
            else:
                element = browser.find_element_by_id(name)
        elif elem_type == "class":
            if index == "all":
                element = browser.find_elements_by_class_name(name)
            else:
                element = browser.find_element_by_class_name(name)
        elif elem_type == "tag":
            if index == "all":
                element = browser.find_elements_by_tag_name(name)
            else:
                element = browser.find_element_by_tag_name(name)
        return element

    # Wait and try again if it failed
    except:
        time.sleep(sleep_time)
        get_element(browser, name, elem_type, index, tries+1)

# Clear the console, set the permit parameters
clear = lambda: os.system('clear')
clear()
if len(sys.argv) == 3:
    group_size = sys.argv[1]
    overnight = sys.argv[2] == "night"
else:
    group_size = 2
    overnight = True
print("Group size has been set to", group_size)
print("Checking for", "overnight" if overnight else "one-day", "permits..")

# Set up the browser and go to the URL
url = 'https://www.recreation.gov/permits/233260'
chrome_options = Options()  
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options = chrome_options)
browser.get(url)

# Choose the Overnight Permit option
division = get_element(browser, 'division-selection-select')
division.click()
dropdown_num = 0 if overnight else 1 
option = get_element(browser, 'rec-select-option-button', 'class', "all")[dropdown_num]
option.click()
time.sleep(0.5)
size_input = get_element(browser, 'number-input')
size_input.send_keys("1")

# Loop through each month
month = ""
total_avaliable = 0
results = ""
while month != "October":

    # Print out the calander month name
    date_element = get_element(browser, 'CalendarMonth__caption')
    date_text_element = get_element(date_element, 'strong', 'tag')
    date_text = date_text_element.get_attribute('innerHTML')
    split = date_text.split(" ")
    month = split[0]
    year = split[1]
    print(month, year)

    # Check free dates here
    grid = get_element(browser, 'js-CalendarMonth__grid', 'class')
    cal_days = get_element(grid, 'rec-available-day', 'class', 'all')
    if len(cal_days) > 0:
        results += month + " " + year + "\n"

    # Print each avaliable day
    for day in cal_days:
        date = get_element(day, 'p', 'tag').get_attribute('innerHTML')
        date_string = month + " " + str(date) + " " + str(year)
        datetime_object = datetime.strptime(date_string, '%B %d %Y')
        day_of_week = calendar.day_name[datetime_object.weekday()][0:2]
        date_printout = date + "-" + day_of_week + " "
        results += date_printout
        print(date_printout, end="")
        total_avaliable += 1
    
    # Print additional information after checking the month for open spots
    if len(cal_days) > 0:
        results += "\n\n"
        print("")
    else:
        print("None Avaliable")

    # Go to the next calander month
    next_button = get_element(browser, 'DayPickerNavigation__next', 'class')
    next_button.click()

# Close the browser
browser.close()

# When all months have been checked, send an email if there were open spots
final = "A total of " + str(total_avaliable) + " permits are avaliable."
print(final)
results = final + "\n\n" + results 
results = results + "https://www.recreation.gov/permits/233260"
if total_avaliable > 0:
    gmail.send(os.environ.get("my_icloud"), "Mt. Whitney Permits Avaliable", results)
