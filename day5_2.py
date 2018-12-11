#!/bin/python3

import string

def reduce(d):
    matchfound = True

    while matchfound:
        s = len(d)
        matchfound = False
        for c in string.ascii_lowercase:
            d = d.replace(c+c.upper(),'')
            d = d.replace(c.upper()+c,'')
            if len(d) < s:
                matchfound = True
    return d

def main():
    d = input()
    l = {}
    for c in string.ascii_lowercase:
        dc = d
        dc = dc.replace(c,'')
        dc = dc.replace(c.upper(),'')
        l[c] = len(reduce(dc))

    print(min(l.values()))
main()
