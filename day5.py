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
            #print(d)
            if len(d) < s:
                matchfound = True
    return d

def main():
    d = input()

    print(len(reduce(d)))
main()
