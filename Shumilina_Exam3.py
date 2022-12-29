print("\nTask1.")


def my_card_protection(card_number, cvc, pincode):
    print('Номер карты:', card_number[:4] + (len(card_number) - 4) * '*')
    print('CVC-код:', len(cvc) * '#')
    print('PIN-код:', (len(pincode) - 1) * '&' + pincode[-1])


my_card_protection(input('Введите номер карты: '), input('Введите CVC-код: '), input('Введите PIN-код: '))

print("\nTask2.")


def decorator(function):
    def wrapper(arg):
        print('Функция:', function.__name__)
        print('Исходные данные:', arg)
        return function(arg)

    return wrapper


@decorator
def is_palindrom(arg):
    return arg == arg[::-1]


print('Результат:', is_palindrom(input('Проверка слова на палиндром.\nВведите слово: ')))

print("\nTask3.")

from abc import abstractmethod


class Company:
    _levels = {1: 'junior', 2: 'middle', 3: 'senior', 4: 'lead'}

    def __init__(self, _index):
        self._index = _index
        self._levels = self._levels[_index]

    def _level_up(self):
        if self._index <= 3:
            self._index += 1
            self._levels = Company._levels[self._index]

    def is_lead(self):
        return self._index == 4

    @abstractmethod
    def test(self):
        pass


class Programmer(Company):
    default_name = 'Anna'
    default_age = 37

    def __init__(self, _index, name=default_name, age=default_age):
        super().__init__(_index)
        self.name = name
        self.age = age

    def work(self):
        if not self.is_lead():
            self._level_up()
        else:
            print('!!!Уровень сотрудника достиг максимального')

    def info(self):
        print(f'\nСотрудник:\nИмя: {self.name}\nВозраст: {self.age}\nКвалификация: {self._levels}')

    def test(self):
        print('\nМетод test добавлен')

    @staticmethod
    def knowledge_base():
        print('''\nA programmer is someone who writes/creates computer software or applications by providing a 
specific programming language to the computer. Most programmers have extensive computing and coding 
experience in many varieties of programming languages and platforms, such as Structured Query Language (SQL), 
Perl, Extensible Markup Language (XML), PHP, HTML, C, C++ and Java. 
    A programmer's most often-used computer 
language (e.g., Assembly, C, C++, C#, JavaScript, Lisp, Python, Java, etc.) may be prefixed to the 
aforementioned terms. Some who work with web programming languages may also prefix their titles with web.''')


# Вариант задания исходных данных с клавиатуры и с использованием значений по умолчанию:
while True:
    level = input('\nВведите уровень сотрудника:\n')
    if level.isdigit() and int(level) in range(1, 5):
        level = int(level)
        break
    else:
        print('Неверный ввод! Введите еще раз:')

Anny = Programmer(level)
Anny.info()
while not Anny.is_lead():
    Anny.work()
    Anny.info()

Anny.test()
# База знаний:
Programmer.knowledge_base()

print("\nTask4.")





class Animal:
    __type_animal = 'Animal'

    def __init__(self, name, colour, height):
        self.name = name
        self.color = colour
        self.height = height

    def info(self):
        print('Животное:', self.__type_animal)
        print('имя:', self.name)
        print('рост:', self.height)

    @staticmethod
    def sound():
        print('Животное издает звуки')


class MyCat(Animal):

    def __init__(self, name, colour, height):
        super().__init__(name, colour, height)


an = Animal('Eddy', 'black', 10)
an.info()
an.sound()
