import sys

def calculate_jumps(distances): 

    # The string is split into a list
    distances = distances.split(" ")

    # The places are initialied to negative one meaning that 
    # it cannot be reached yet. Index zero is set to zero because
    # that's where we start
    places = [sys.maxsize] * (len(distances) + 1)
    places[0] = 0

    # Gets the number of places
    num_places = len(distances)
  
    # For each place except for the first one, which is already zero
    for current in range(1, num_places):
        
        # Look at all previous places
        for prev in range(current): 

            # Convert the distance from the input str to an int
            distances[prev] = int(distances[prev])

            # If the jumps to the current place is less than the distance to the 
            # previous plus the distance you can jump from the previous, then update
            # the distance it takes to get to the current place.
            if (current <= prev + distances[prev]): 
                if places[current] == -1:
                    places[current] = places[prev] + 1
                else:
                    places[current] = min(places[current], places[prev] + 1) 
                break

    # Get the number of jumps to the last place and print
    dist_to_last = places[num_places-1]
    if dist_to_last == sys.maxsize:
        print(-1)
    else:
        print(dist_to_last)

num_places = int(input())
places_string = input()
calculate_jumps(places_string)
