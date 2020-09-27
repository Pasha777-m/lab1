from collections import deque # імпортування бібліотеки deque
import unittest #імпортування бібліотеки unittest для подальшої реалізації тестів
a=[5,-9,756,86,-48,9,7] #створення статичного масиву
class myClass(): #створення загального класу
    def array(): #створення функції
        sum = 0 #декларуємо sum
        k = 0 #декларуємо k
        for i in range(len(a)): #цикл для визначення довжини масиву а
            sum  = a[i] #визначення всіх елементів масиву
            k += 1 #шукаємо довжину масиву
        print(a) #виводимо наш масив
        return k #повертаємо k
    print("кількість елементів в списку:", array()) #виводимо к-ть елементів масиву
    def queue(a): #створення функції
        d = deque(a, maxlen=7) #створення черги
        sum1 = 0 #декларуємо sum1
        p = 0 #декларуємо р
        for i in range(len(d)): #цикл для визначення довжини черги d
            sum1  = d[i] #визначення всіх елементів черги
            p += 1  #шукаємо довжину черги       
        print(d) #виводимо нашу чергу
        return p #повертаємо р
    print("кількість елементів в черзі:", queue(a)) #виводимо к-ть елементів черги

class MyTest(unittest.TestCase): #створення класу для реалізації тестів
    def test_usage1(self):#створення функції для тесту
        self.assertEqual(myClass.array(),7)#використання команди self.assertEqual() для порівняння довжини масиву

    def test_usage2(self):#створення функції для тесту 2 
        self.assertEqual(myClass.queue(a),7)#використання команди self.assertEqual() для порівняння довжини черги
        
if __name__ == "__main__":
    unittest.main()#команда яка запускає всі тести із заданого модуля