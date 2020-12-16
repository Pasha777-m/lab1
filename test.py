from collections import deque
import unittest as ut
import random
import lab2_Minyuk as pt

class MyTest(ut.TestCase):
    
    def setUp(self):
        self.mp=pt.MyClass()
        
    def test_usage1(self):
        self.assertEqual(self.mp.array(),7)

    def test_usage2(self):
        self.assertEqual(self.mp.queue(),7)

    def test_usage3(self):
        self.assertRaises(Exception,self.mp.add)
        
    def test_usage4(self):
        self.assertRaises(Exception,self.mp.remove)
       
if __name__ == "__main__":
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    ut.main(testRunner=runner)
    ut.main()
