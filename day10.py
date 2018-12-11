#!/bin/python3

# Gives a lot of false positives

import sys,re

def manhatdist(c1, c2):
    return abs(c1[0]-c2[0])+abs(c1[1]-c2[1])

def printpoints(points):
    tmpx = []
    tmpy = []
    # find minx miny maxx maxy
    for p in points:
        tmpx.append(p[0])
        tmpy.append(p[1])

    miny = min(tmpy)
    minx = min(tmpx)
    maxy = max(tmpy)
    maxx = max(tmpx)

    for y in range(miny-2,maxy+2):
        for x in range(minx-2,maxx+2):
            if [x,y] in points:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')
    sys.stdout.write('\n')
 
    

def main():
    p = re.compile(r'[-]?\d+')
    data = []
    points = []
    deltav = []

    # Read input to list
    for line in sys.stdin:
        data.append(list(map(int, p.findall(line))))

    # Split points and velocity
    for d in data:
        points.append([d[0],d[1]])
        deltav.append([d[2],d[3]])
    l = len(deltav)

    notfound = True
    second = 0
    while notfound:
        for p1 in points:
            plausible = False
            for p2 in points:
                

                if p1 != p2:
    #                if second == 10027:
    #                    print(p1,p2,manhatdist(p1,p2))
                    if manhatdist(p1, p2) <= 2:
                        plausible = True
                        break
            if not plausible:
                notfound = True
                break
            else:
                print("found!",second)
                printpoints(points)
                break

        for i in range(0,l):
            points[i][0] += deltav[i][0]
            points[i][1] += deltav[i][1]
        second += 1


main()
