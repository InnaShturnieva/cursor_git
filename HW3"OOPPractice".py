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


