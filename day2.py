#!/bin/python3

import sys

def main():
    twos = 0
    threes = 0

    for line in sys.stdin:
        d = {}
        for c in set(line.strip()):
            d[c] = line.count(c)
        if 2 in d.values():
            twos += 1
        if 3 in d.values():
            threes += 1

    print("Checksum: ", twos * threes)
main()
