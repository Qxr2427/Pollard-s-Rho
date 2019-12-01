#!/usr/bin/python2.7
# David Cox 2016
from fractions import gcd
import random

def pollards_rho(n):
    x = random.randint(2,n-2); y = x; d = 1; c=random.randint(1,n-1)
    f = lambda x: (x**2 + c) % n
    while d == 1:
        x = f(x); y = f(f(y))
        d = gcd(abs(x-y), n)
    if d != n: return d

n = 349810984018843*349810984018901
print(n)
start = __import__("time").time()
p = pollards_rho(n)
end = __import__("time").time()

print(p)
print(end - start)
