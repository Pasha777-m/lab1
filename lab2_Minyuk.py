from collections import deque 
import unittest

a=[5,-9,756,86,-48,9,7]
d = deque(a, maxlen=7)
a1=[]
b = deque(a1)

class myClass():
    
    def array(): 
        sum = 0 
        k = 0 
        for i in range(len(a)): 
            sum  = a[i] 
            k += 1 
        print(a) 
        return k    
    print("кількість елементів в списку:", array())
    
    def queue(a): 
        sum1 = 0 
        p = 0 
        for i in range(len(d)):
            sum1  = d[i] 
            p += 1         
        print(d)
        return p    
    print("кількість елементів в черзі:", queue(a))
    
    def add(d):
        d.append(777)
        print(d)
        return d

    def empty(b):
        d.pop()
        print(b)
        return b
        
class MyTest(unittest.TestCase): 
    def test_usage1(self):
        self.assertEqual(myClass.array(),7)

    def test_usage2(self):
        self.assertEqual(myClass.queue(a),7)

    def test_usage3(self):
        self.assertTrue(myClass.add(d))

    def test_usage4(self):
        self.assertFalse(myClass.empty(b))
        
if __name__ == "__main__":
    unittest.main()
