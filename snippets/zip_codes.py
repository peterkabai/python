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

