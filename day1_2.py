#!/bin/python3

import sys

def main():
    c = 0
    p = 0
    seen = []
    data = []
    for line in sys.stdin:
        data.append(line.strip())
    s = len(data)

    while True:
        c += int(data[p])

        if c in seen:
            break
        else:
            seen.append(c)
   
        p = (p + 1) % s

    print("Twice: " + str(c))

main()
