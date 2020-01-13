'''
Внимание! Поскольку время выполнения округляется до 5-го знака после запятой,
то время выполнения коротких функций может быть равно 0.


Пример использования кода при копировании класса прямо в скрипте.

def test(a, b):
        print("This is a - {}".format(a))
        print("This is b - {}".format(b))    
    
with TestTimer() as testtimer:
    test("2", "3")



Пример использования кода при импорте отдельным модулем.

import ContextModuleScript

def test(a, b):
        print("This is a - {}".format(a))
        print("This is b - {}".format(b))    
    
with ContextModuleScript.TestTimer() as testtimer:
    test("2", "3")
'''

# Импорт модулей

import time


# Создание класса

class TestTimer():
    def __enter__(self):
        self.start_timer = time.time()
        return self
    
    def timer(self):
        self.avg_timer = self.end_timer - self.start_timer
        print("Время выполнения скприта -  %.5f секунд" % self.avg_timer)
        
    def __exit__ (self, *args):
        self.end_timer = time.time()
        return self.timer()