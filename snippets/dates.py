from datetime import date
from datetime import datetime
import calendar

# Print the day of week today
todays_date = date.today()
print (calendar.day_name[todays_date.weekday()])

# Convert date string to date, print day of week
string ="April 10 2019"
datetime_object = datetime.strptime(string, '%B %d %Y')
print (calendar.day_name[datetime_object.weekday()])
