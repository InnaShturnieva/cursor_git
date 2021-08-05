from abc import ABC, abstractmethod
import random

class Human (ABC):
    @abstractmethod
    def info(self):
        pass
    @abstractmethod
    def make_money(self, salary):
        pass
    @abstractmethod
    def buy_house(self, house):
        pass


class Person (Human):
    def __init__(self, name, age, money, own_home: list):
        self.name = name
        self.age = age
        self.money = money
        self.own_home = own_home

    def info(self):
        print(f"Person name is {self.name}.He is {self.age} years old. '\n'"
              f"He has money savings in the amount of: {self.money} dollars. He has {self.own_home} own home")

    def make_money(self, salary):
        self.money += salary
        print(f"After salary his money savings is amount of: {self.money}.")

    def buy_house(self, house):
        if self.money >= house.cost:
            self.own_home.append(house)
            print("Person can buy a house")
        else:
            print("Person can't buy this house")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost


class SmallHouse(House):
    def __init__(self, cost, area=40):
        super().__init__(area, cost)


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):

    def __init__(self, name, houses: list, discount):
        self.name = name
        self.houses = houses
        self.discount = discount


    def info_of_houses (self):
        print(f"Realtor {self.name} can offer to you buy such a houses: {self.houses}")
        for house in self.houses:
             print (f'The area of house is {house.area}, it costs {house.cost}')

    def discount(self):
        return self.discount

    @staticmethod
    def stealing(person):
        stolen = round(float(person.money * random.uniform(0, 0.10)), 2)
        person.money -= stolen
        return f'Realtor stole {stolen} amount of money. Currently {person.name} has {person.money}'

    def sold_house(self, house):
        self.houses.remove(house)


realtor = Realtor('Monika', ['house1', 'house2', 'house3'], 0.1)
person = Person('Chendler', 38, 100000, ['appartament'])
house1 = House(70, 50000)
house2 = House(50, 33000)
house3 = House(100, 120000)
person.info()
realtor.info_of_houses()
realtor.discount(house3)
person.buy_house(house3)
realtor.stealing(person)
