#!/bin/python3

import sys

def compstr(s1, s2):
    diff = 0
    for x in range(len(s1)):
        if s1[x] != s2[x]:
            diff += 1
    return diff

def main():
    d = []
    comp = []
    for line in sys.stdin:
        d.append(line.strip())

    for x in range(len(d)-1):
        for y in range(len(d)-1):
            if not d[x] == d[y]:
                comp.append( [ d[x], d[y], compstr(d[x],d[y]) ] )

    lowest = 1000   
    pos = 0
    for x in range(len(comp)):
        if comp[x][2] < lowest:
            pos = x
            lowest = comp[x][2]
    
    print(comp[pos][0])
    print(comp[pos][1])

main()
