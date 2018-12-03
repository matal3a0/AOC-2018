#!/bin/python3

import sys

def main():
    fabric = [[0 for i in range(1000)] for i in range(1000)]
    overlaps = 0

    for line in sys.stdin:
        d = line.strip().split()
        startx = int(d[2].split(',')[0])
        starty = int(d[2].split(',')[1].replace(':',''))
        x = int(d[3].split('x')[0])
        y = int(d[3].split('x')[1])

        for a in range(startx,startx+x):
            for b in range(starty,starty+y):
                fabric[a][b] += 1

    for a in range(1000):
        for b in range(1000):
            if fabric[a][b] >= 2:
                overlaps += 1
        
    print("Overlaps: ", overlaps)
main()
