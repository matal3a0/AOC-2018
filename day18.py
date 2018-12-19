#!/bin/python3

import sys,copy

def main():
    loops = 10

    acres = []
    for line in sys.stdin:
        acres.append(list(x for x in line if x != '\n'))
    size = len(acres[0])

    for l in range(0,loops):
        acres_copy = copy.deepcopy(acres)
        for y in range(0,size):
            for x in range(0,size):
                s = { '|': 0, '#': 0, '.': 0 }
                for b in range(y-1,y+2):
                    for a in range(x-1,x+2):
                        if a != x or b != y: # dont check current
                            if a >= 0 and b >= 0 and a < size and b < size: # stay inside!
                                s[acres[b][a]] += 1
                
                if acres[y][x] == '.' and s['|'] >= 3:
                    acres_copy[y][x] = '|'
                elif acres[y][x] == '|' and s['#'] >= 3:
                        acres_copy[y][x] = '#'
                elif acres[y][x] == '#':
                    if s['#'] >= 1 and s['|'] >= 1:
                        acres_copy[y][x] = '#'
                    else:
                        acres_copy[y][x] = '.'
                else:
                    acres_copy[y][x] = acres[y][x]

        acres = copy.deepcopy(acres_copy)

    s = { '|': 0, '#': 0, '.': 0 }
    for y in range(0,size):
        for x in range(0,size):
            s[acres[y][x]] += 1

    print(s['|'] * s['#'])


main()
