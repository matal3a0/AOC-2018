#!/bin/python3

import sys

def main():
    d = []
    carts = []
    crash = False
    steps = 0

    for line in sys.stdin:
        d.append(list(x for x in line if x != '\n'))

    for y in range(0,len(d)):
        for x in range(0,len(d[0])):
            if d[y][x] in ['<','>','^','v']:
                carts.append([ y, x, d[y][x], 'l' ])

    while len(carts) > 1:
        steps += 1
        carts.sort()
        cartscopy = carts[:] # Copy by value, not reference
        for c in carts:
            if c[2] == '<':
                c[1] -= 1
                if d[c[0]][c[1]] == '/':
                    c[2] = 'v'
                elif d[c[0]][c[1]] == '\\':
                    c[2] = '^'
                elif d[c[0]][c[1]] == '+':
                    if c[3] == 'l':
                        c[3] = 's'
                        c[2] = 'v'
                    elif c[3] == 's':
                        c[3] = 'r'
                        c[2] = '<'
                    elif c[3] == 'r':
                        c[3] = 'l'
                        c[2] = '^'
            elif c[2] == '>':
                c[1] += 1
                if d[c[0]][c[1]] == '/':
                    c[2] = '^'
                elif d[c[0]][c[1]] == '\\':
                    c[2] = 'v'
                elif d[c[0]][c[1]] == '+':
                    if c[3] == 'l':
                        c[3] = 's'
                        c[2] = '^'
                    elif c[3] == 's':
                        c[3] = 'r'
                        c[2] = '>'
                    elif c[3] == 'r':
                        c[3] = 'l'
                        c[2] = 'v'
            elif c[2] == '^':
                c[0] -= 1
                if d[c[0]][c[1]] == '/':
                    c[2] = '>'
                elif d[c[0]][c[1]] == '\\':
                    c[2] = '<'
                elif d[c[0]][c[1]] == '+':
                    if c[3] == 'l':
                        c[3] = 's'
                        c[2] = '<'
                    elif c[3] == 's':
                        c[3] = 'r'
                        c[2] = '^'
                    elif c[3] == 'r':
                        c[3] = 'l'
                        c[2] = '>'
            elif c[2] == 'v':
                c[0] += 1
                if d[c[0]][c[1]] == '/':
                    c[2] = '<'
                elif d[c[0]][c[1]] == '\\':
                    c[2] = '>'
                elif d[c[0]][c[1]] == '+':
                    if c[3] == 'l':
                        c[3] = 's'
                        c[2] = '>'
                    elif c[3] == 's':
                        c[3] = 'r'
                        c[2] = 'v'
                    elif c[3] == 'r':
                        c[3] = 'l'
                        c[2] = '<'

            for c2 in carts:
                if c != c2:
                    if c[0] == c2[0] and c[1] == c2[1]:
                        crash = True
                        cartscopy.remove(c2)
                        cartscopy.remove(c)
            carts = cartscopy[:]

    print(str(carts[0][1]) + ',' + str(carts[0][0]))
main()
