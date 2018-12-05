#!/bin/python3

def reduce(d):
    matchfound = True

    while matchfound:
        i = 0
        s = len(d)
        matchfound = False
        while(i < s-1):
            if not d[i] == d[i+1]:
                if d[i].lower() == d[i+1] or d[i].upper() == d[i+1]:
                    matchfound = True
                    d = d[:i] + d[i+2:]
            i = (i + 1) % s
            s = len(d)
    return d

def main():
    d = input()

    print(len(reduce(d)))
main()
