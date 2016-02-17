'''
USCD - Algorithmic Toolbox - Week 1, Assignment 2

Attempt to build a code with a stress test component:

We code up 2 different solutions sol_a, sol_b (both same in this instance)
and then via a number generator, feed both solutions with the same arg a.
Iterate and then check outputs for differences.
Break the loop if there is a difference in solutions (obviously none),
Otherwise print 'OK' at end of each test indicate that our solutions are equal.
'''

import numpy as np

# n = int(input())
# a = [int(x) for x in input().split()]
# assert(len(a) == n)

def sol_a(a):
    result = 0
    l = len(a)
    for i in range(0, l):
        for j in range(i+1, l):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    print(result)

def sol_b(a):
    result = 0
    l = len(a)
    for i in range(0, l):
        for j in range(i+1, l):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    print(result)

c = 0
while (c < 5):
    n = np.random.randint(1,1000,
                          np.mod(np.random.randint(1000), 5) + 2)
    a = [n[i:i+1] for i in range(0,len(n),1)]
    if sol_a(a) != sol_b(a):
        print('Error!') # not going to happen
        break
    else:
        print('OK')
    c += 1

