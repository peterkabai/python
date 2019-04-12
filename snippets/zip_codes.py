from uszipcode import SearchEngine

# Create the engine to search for zip codes
search = SearchEngine(simple_zipcode = True)

# Get the info for one specific zipcode
zipcode = 94404
zip_info = search.by_zipcode(str(zipcode))

# Get specific info from the zipcode class
coord = zip_info.lat, zip_info.lng
state = zip_info.state
county = zip_info.county
city = zip_info.major_city

# Print the results
print(city, county, state, coord, sep=", ")

# Here's a function to store zipcode and county name in a map
# It speeds up the search time when there are many duplicate zip codes
county_zip = {}
def find_county(zip):
    if zip in county_zip: 
        return county_zip[zip]
    else:
        county = search.by_zipcode(str(zip)).county
        county_zip[zip] = county
        return county

# Same as above, but for states
state_zip = {}
def find_state(zip):
    if zip in state_zip: 
        return state_zip[zip]
    else:
        state = search.by_zipcode(str(zip))
        state_zip[zip] = state
        return state

# Let's test the above function on a list of zipcodes
zips = ["94404","90210","95020"]
counties = [find_county(z) for z in zips]
print(counties)

zips = ["94404","90210","95020"]
states = [find_state(z) for z in zips]
print(states)
