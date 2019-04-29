

from sys import stdin 
import math

cases = int(stdin.readline())


case = 0
while case < cases:
    price = 0

    line = [int(x) for x in stdin.readline().split(' ')]
    rides = line[0]
    k = line[1]
    n = line[2]

    in_line = [int(x) for x in stdin.readline().split(' ')]
    initial = str(in_line)
    
    ride = 0
    while ride < rides:

        people = 0

        i = 0
        while i < n:
            g = in_line[0]
            if g + people <= k:
                people += g
                in_line.append(in_line[0])
                del in_line[0]

            else:
                break
            i += 1

        price += people
        ride += 1

        # When this happens, we've returned to the initial state of the line
        if str(in_line) == initial:
            multiple = math.floor(rides/ride)
            price = price * multiple
            ride = multiple * ride

    print("Case #", case+1, ": ",price, sep="")
    case += 1