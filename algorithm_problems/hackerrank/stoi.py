#! /usr/bin/python3

def stoi(s):
    c = int(s[0])
    s = s[1:]
    if s:
        return c * 10**len(s) + stoi(s)
    return c * 10**len(s)
   
print(stoi("12345"))
print(stoi("72739854"))
