#!/bin/python3

import sys

def makegrid(gsn):
    grid = [[0 for y in range(301)] for x in range(301)]

    for y in range(1,301):
        for x in range(1,301):
            rackid = x + 10
            pwlvl = rackid * y
            pwlvl += gsn
            pwlvl = pwlvl * rackid
            pwlvl = ((pwlvl // 100) % 10)
            pwlvl -= 5
            grid[x][y] = pwlvl

    return grid

def printgrid(grid,startx,starty,size):
    for y in range(starty,starty+size):
        for x in range(startx,startx+size):
            sys.stdout.write(str(x)+','+str(y)+': '+str(grid[x][y])+'\t')
        sys.stdout.write('\n')

def maxpower(grid,size):
    maxx = 0
    maxy = 0
    maxpower = 0
    for y in range(1,299):
        for x in range(1,299):
            totalpower = 0
            for xi in range(size):
                for yi in range(size):
                    if x+xi < 300-xi and y+yi < 300-yi:
                        totalpower += grid[x+xi][y+yi]

            if totalpower > maxpower:
                maxpower = totalpower
                maxx = x
                maxy = y

    return maxx,maxy,maxpower

def main():
    grid = makegrid(5177)
    absolutetotalmaxpower = 0
    maxx = 0
    maxy = 0
    maxsize = 0

    for size in range(301):
        x,y,maxp = maxpower(grid,size)
        if maxp > absolutetotalmaxpower:
            maxx = x
            maxy = y
            maxsize = size
            absolutetotalmaxpower = maxp

    print(maxx,maxy,maxsize)

main()
