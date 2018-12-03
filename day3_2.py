#!/bin/python3

import sys

def main():
    fabric = [[[0, 0, False] for i in range(1000)] for i in range(1000)]
    data = set()
    lc = 0

    for line in sys.stdin:
        data.add(line)

    for line in data:
        d = line.strip().split()
        cid = int(d[0].split('#')[1])
        startx = int(d[2].split(',')[0])
        starty = int(d[2].split(',')[1].replace(':',''))
        x = int(d[3].split('x')[0])
        y = int(d[3].split('x')[1])

        for a in range(startx,startx+x):
            for b in range(starty,starty+y):
                fabric[a][b][0] = cid
                fabric[a][b][1] += 1
                if fabric[a][b][1] > 1:
                    fabric[a][b][2] = True

    for line in data:
        overlap = False
        d = line.strip().split()
        cid = int(d[0].split('#')[1])
        startx = int(d[2].split(',')[0])
        starty = int(d[2].split(',')[1].replace(':',''))
        x = int(d[3].split('x')[0])
        y = int(d[3].split('x')[1])

        for a in range(startx,startx+x):
            for b in range(starty,starty+y):
                if fabric[a][b][2]:
                    overlap = True
        if not overlap:
            print("Id", cid)
main()
