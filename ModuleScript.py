'''
Внимание! Поскольку время выполнения округляется до 5-го знака после запятой,
то время выполнения коротких функций может быть равно 0.
Для получения видимых значений рекомендую указать параметр trying побольше, например 100.


Пример использования кода при копировании класса прямо в скрипте.

@TestTimer
def test(a, b):
    print("This is a - {}".format(a))
    print("This is b - {}".format(b))

test.timer("first argument (a)", "second argument (b)", trying = 5)

trying - опциональный аргумент, если его не указывать, функция выполнится один раз.



Пример использования кода при импорте отдельным модулем.

import ModuleScript

@ModuleScript.TestTimer
def test(a, b):
    print("This is a - {}".format(a))
    print("This is b - {}".format(b))

test.timer("first argument (a)", "second argument (b)", trying = 5)
'''

# Импорт модулей

import time


# Создание класса

class TestTimer():
    def __init__(self, function):
        self.run = function
    
    def timer(self, *args, trying = 1):
        self.trying = trying # Опциональный аргумент, влияет на количество запусков
        self.start_timer = time.time()
        for i in range(self.trying):
            self.run(*args)
        self.end_timer = time.time()
        self.avg_timer = self.end_timer - self.start_timer
        print("Количество выполнений скрипта {}".format(self.trying))
        print("Общее время выполнения -  %.5f секунд" % self.avg_timer)
        print("Среднее время выполнения %.5f секунд" % (self.avg_timer / self.trying))