#!/bin/python3

import sys,re,operator
from collections import defaultdict,Counter

def main():
    data = []
    guards = []
    schedule = defaultdict(list)
    
    for line in sys.stdin:
        data.append(re.findall(r"[\w']+", line))
    data.sort()
    
    for d in data:
        if d[5] == 'Guard':
            guard = int(d[6])
        elif d[5] == 'falls':
            startsleep = int(d[4])
        elif d[5] == 'wakes':
            endsleep = int(d[4])
            for minute in range(startsleep,endsleep):
                schedule[guard].append(minute)
    
    for k, v in schedule.items():
        count = dict(Counter(v))
        totsleep = sum(count.values())
        bestminute = max(count.items(), key=operator.itemgetter(1))[0]
        guards.append([totsleep,k,bestminute])
    
    best = max(guards)
    print(best[1]*best[2])

main()
