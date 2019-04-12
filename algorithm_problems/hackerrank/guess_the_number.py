#! /usr/bin/python3

# https://csumb.kattis.com/problems/guess

guess_num = 1
guess = 500
low = 1
high = 1000

while guess_num <= 10:
    print(guess)
    response = input()
    if response == "lower":
        high = guess-1
        guess = round((high + low) / 2)
    elif response == "higher":
        low = guess+1
        guess = round((high + low) / 2)
    else:
        break
    guess_num += 1
        