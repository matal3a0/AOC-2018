#!/bin/python3

import sys
def printstate(state):
    for x in range(-3,len(state)-3):
        sys.stdout.write(state[x])
    sys.stdout.write('\n')

def main():
    d = []
    ops = []
    state = ['.' for x in range(0,200)]
    count = 0

    # input
    for line in sys.stdin:
        d.append(line.strip().split())
    
    # init state
    for x in range(0,len(d[0][2])):
        state[x] = d[0][2][x]

    for i in range(2,len(d)):
        ops.append([d[i][0],d[i][2]])

    for gen in range(0,20):
        newstate = ['.' for x in range(0,200)]
        for x in range(-30,198):
            stringtotest = state[x-2]+state[x-1]+state[x]+state[x+1]+state[x+2]
            for m,r in ops:
                if stringtotest == m:
                    print(x,'match',stringtotest,'==',m,'->',r)
                    newstate[x] = r 
                    break
                else:
                    newstate[x] = '.'
        state = newstate
        print(gen)
        printstate(state)

    for x in range(-30,198):
        if state[x] == '#':
            count += x

    print(count)
main()
