#!/bin/python
"""
Demo of two ways of using multiprocessing in python
"""

import multiprocessing as mp

"""
Using queue to communicate processes results
"""

def f1(x, q):
    q.put(x**2)
    return

q = mp.Queue()
processes = []
for x in range(4):
    processes.append(mp.Process(target=f1, args=(x,q)))


for p in processes:
    p.start()

for p in processes:
    p.join()

while(not q.empty()):
    print(q.get())


"""
Using pool of processes
"""

def f2(x):
    return x**2

pool = mp.Pool(processes=4)
inputs = range(4)
outputs = pool.map(f2, inputs)
print (outputs)