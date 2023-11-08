# Purpose: learn about time
# How: borrowed code
# Status: works
# Elements: time, range, for
# Imports: time
# Author: finxter
# Date: null
# Note: 
#______________________________________________________________________
import time
def f1(n):
    return ''.join([str(x) for x in range(n)])

def f2(n):
    s = ''
    for x in range(n):
        s += str(x)
    return s

n = 10**6
t1 = time.time()
f1(n)
print(n)
print(t1)
t2 = time.time()
f2(n)
print(n)
print(t2)
t3 = time.time()
print(n)
print(t3)

print(t3 - t2 > t2 - t1)