keys = {
    "a": 2,
    "b": 22,
    "c": 222,
    "d": 3,
    "e": 33,
    "f": 333,
    "g": 4,
    "h": 44,
    "i": 444,
    "j": 5,
    "k": 55,
    "l": 555,
    "m": 6,
    "n": 66,
    "o": 666,
    "p": 7,
    "q": 77,
    "r": 777,
    "s": 7777,
    "t": 8,
    "u": 88,
    "v": 888,
    "w": 9,
    "x": 99,
    "y": 999,
    "z": 9999,
    " ": 0
}

num_strings = int(input())

for i in range(1, num_strings+1):
    string = input()
    print("Case #",i,": ", end="", sep="")
    prev = "*"
    for c in string:

        curr = keys[c]
        if str(curr)[0] == prev:
            print(" ", end="")
        print(curr, end="")

        prev = str(curr)[0]
    print("")
