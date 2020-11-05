from collections import deque
import numpy as np
import random

a = [5,-9,756,86,-48,9,7]
a1 = []
d = deque(a, maxlen=7)
d1 = deque(a1)

class MyClass():
    def array(self): 
        sum = 0 
        k = 0 
        for i in range(len(a)): 
            sum  = a[i] 
            k += 1 
        print(a) 
        return k    
    #print("кількість елементів в списку:", array(self))

    def queue(self): 
        sum1 = 0 
        p = 0 
        for i in range(len(d)):
            sum1  = d[i] 
            p += 1         
        print(d)
        return p
    #print("кількість елементів в черзі 1:", queue(self))
    #print(d1)
    #print("кількість елементів в черзі 2:", len(d1))

    def add(self):
        if d.maxlen == len(d):
            raise Exception
        d.insert(0, -777)

    def remove(self):
        if d1.maxlen == len(d1):
            raise Exception
        d1.pop()

#print(dir(d))
