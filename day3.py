#!/bin/python3

import sys,re

def main():
    fabric = [[0 for i in range(1000)] for i in range(1000)]
    overlaps = 0

    for line in sys.stdin:
        p = re.compile(r'\d+')
        d = p.findall(line)

        sx = int(d[1])
        sy = int(d[2])
        x = int(d[3])
        y = int(d[4])

        for a in range(sx,sx+x):
            for b in range(sy,sy+y):
                fabric[a][b] += 1

    for a in range(1000):
        for b in range(1000):
            if fabric[a][b] >= 2:
                overlaps += 1
        
    print("Overlaps: ", overlaps)
main()
