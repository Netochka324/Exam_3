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
    __update_by_courses = True
    __degree_by_courses = 1

    def __init__(self, _index):
        self._index = _index
        self._levels = self._levels[_index]

    def __level_up_by_courses(self):
        if Company.__update_by_courses:
            self._index += Company.__degree_by_courses

    def _level_up(self):
        Company.__level_up_by_courses(self)
        if self._index <= 3:
            self._index += 1
            self._levels = Company._levels[self._index]
        else: self._levels = Company._levels[4]

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

    def info(self):
        print(f'\nСотрудник:\nИмя: {self.name}\nВозраст: {self.age}\nКвалификация: {self._levels}')

    def test(self):
        print('\nМетод test добавлен')

    @staticmethod
    def knowledge_base():
        print('''\nA programmer is someone who writes/creates computer software or applications by providing a
        specific programming language to the computer. Most programmers have extensive computing and coding
        experience in many varieties of programming languages and platforms, such as Structured Query Language (SQL),
        Perl, Extensible Markup Language (XML), PHP, HTML, C, C++ and Java. A programmer's most often-used computer
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
    name_default = '<empty>'
    __type = 'животное'
    Group_animal = 'Группа: домашнее ' + __type

    def __init__(self, name=name_default):
        self.name = name
        print(f"\nРодилось {Animal.__type}.")

    def eat(self):
        print(f'{self.name} хочет есть. {self.name} ням-ням')

    def sleep(self):
        print(f'{self.name} хочет спать. {self.name} хрррррр...')

    def __make_noise(self):
        return "...грр"

    def info(self):
        print('Класс:', Animal.__type)
        print('Кличка:', self.name)
        if self.name == Animal.name_default: print('Дайте животному кличку!')
        print('Издает звуки:', self.__make_noise())

    @staticmethod
    def animals_info():
        print('Кошки и собаки - наиболее распространенные домашние животные.')

    @classmethod
    def group_animal(cls):
        return cls.Group_animal


class Cat(Animal):
    __type = 'кот'
    Group_animal = 'Группа: домашний ' + __type

    def __init__(self, name):
        super().__init__(name)
        print(f"Родился {Cat.__type}!")

    def __make_noise(self):
        return "...мяу"

    def info(self):
        print('Класс:', Cat.__type)
        print('Кличка:', self.name)
        print('Издает звуки:', self.__make_noise())

    @staticmethod
    def cats_info():
        print('''Кошка (Felis catus) - домашний вид мелких плотоядных млекопитающих. Это единственный одомашненный 
        вид в семействе кошачьих, и его часто называют домашней кошкой, чтобы отличить его от диких членов семейства. 
        Кошка может быть домашней кошкой, фермерской кошкой или дикой кошкой; последняя свободно передвигается и 
        избегает контакта с человеком.''')


class Dog(Animal):
    __type = 'собака'
    Group_animal = 'Группа: домашняя ' + __type

    def __init__(self, name):
        super().__init__(name)

    def __make_noise(self):
        return "...гав"

    def info(self):
        print('Класс:', Dog.__type)
        print('Кличка:', self.name)
        print('Издает звуки:', self.__make_noise())

    @staticmethod
    def dogs_info():
        print('''С зоологической точки зрения, собака — плацентарное млекопитающее отряда хищных семейства псовых. 
        Собаки известны своими способностями к обучению, любовью к игре, социальным поведением. Выведены специальные 
        породы собак, предназначенные для различных целей: охоты, охраны, тяги гужевого транспорта и другого, 
        а также декоративные породы (например, болонка, пудель).''')


obj = Animal('Маша')
print(Animal.group_animal())
obj.info()
obj.eat()
obj.sleep()
Animal.animals_info()

obj1 = Cat('Мурка')
obj1.info()
obj1.eat()
Cat.cats_info()

obj2 = Dog('Шарик')
print(obj2.group_animal())
obj2.info()
obj2.eat()
obj2.sleep()
Dog.dogs_info()

obj3 = Animal()
obj3.info()

obj4 = Cat('Гномик')
print(obj4.group_animal())
obj4.info()
