#!/bin/python3

import sys

def main():
    data = []
    for line in sys.stdin:
        data.append(int(line))

    print("Sum: " + str(sum(data)))

main()
