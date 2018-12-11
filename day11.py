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

def maxpower(grid):
    maxx = 0
    maxy = 0
    maxpower = 0
    for y in range(1,299):
        for x in range(1,299):
            totalpower = grid[x][y] + grid[x+1][y] +grid[x+2][y] +grid[x][y+1] +grid[x+1][y+1] +grid[x+2][y+1] +grid[x][y+2] +grid[x+1][y+2] +grid[x+2][y+2]
            if totalpower > maxpower:
                maxpower = totalpower
                maxx = x
                maxy = y

    print(str(maxx)+','+str(maxy))


def main():
    grid = makegrid(5177)

    maxpower(grid)

main()
