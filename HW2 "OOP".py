# Task 1
print("Task 1")


class Animals:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.__class__.__name__} {self.name} is eating")

    def sleep(self):
        print(f"{self.__class__.__name__} {self.name} is sleeping")


class Lion (Animals):
    def hunt(self):
        print(f"{self.__class__.__name__} {self.name} is hunting")


class Dog(Animals):
    def serve(self):
        print(f"{self.__class__.__name__} {self.name} is serving")


class Cat(Animals):
    def speak(self, sound):
        return f"{self.name} says: {sound}"


class Kangaroo(Animals):
    def jump(self):
        print(f"{self.__class__.__name__} {self.name} is jumping")


class Tiger(Animals):
    def run(self):
        print(f"{self.__class__.__name__} {self.name} is running")


simba = Lion("Simba")
print(simba.hunt(), simba.eat(), simba.sleep(), sep='\n')
bobik = Dog("Bobik")
print(bobik.serve(), bobik.eat(), bobik.sleep(), sep='\n')
murka = Cat("Murka")
print(murka.speak("Meow"), murka.eat(), murka.sleep(), sep='\n')
felix = Kangaroo("Felix")
print(felix.jump(), felix.eat(), felix.sleep(), sep='\n')
tony = Tiger("Tony")
print(tony.run(), tony.eat(), tony.sleep(), sep='\n')


print(f"Simba is instance of Animals:", {isinstance(simba, Animals)})
print(f"Bobik is instance of Animals:", {isinstance(bobik, Animals)})
print(f"Murka is instance of Animals:", {isinstance(murka, Animals)})
print(f"Felix is instance of Animals:", {isinstance(felix, Animals)})
print(f"Tony is instance of Animals:", {isinstance(tony, Animals)})


# Task 1.a
print("Task 1.a")


class Human:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.__class__.__name__} {self.name} is eating")

    def sleep(self):
        print(f"{self.__class__.__name__} {self.name} is sleeping")

    def study(self):
        print(f"{self.__class__.__name__} {self.name} is studying")

    def work(self):
        print(f"{self.__class__.__name__} {self.name} is working")


class Centaur(Human, Lion):
    def cook(self):
        print(f"{self.__class__.__name__} {self.name} is cooking")

    def hunt(self):
        return super().hunt()


centaur = Centaur("Abas")
print(centaur.hunt(), centaur.cook(), centaur.sleep(), centaur.work(), centaur.study(), centaur.eat(), sep='\n')
