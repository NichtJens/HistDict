#!/usr/bin/env python

import random
random.seed(0)

def throw1dice():
    return random.randint(1, 6)

def throwNdice(N):
    return sum(throw1dice() for _ in range(N))


from histdict import HistDict

HD1 = HistDict()
HD2 = HistDict()

for _ in range(10000):
    HD1.fill(throw1dice())
    HD2.fill(throwNdice(2))

print HD1.posMax, HD1.mean, HD1.stddev
print HD2.posMax, HD2.mean, HD2.stddev


from matplotlib import pyplot as plt

plt.plot(*HD1.xy)
plt.plot(*HD2.xy)
plt.show()



