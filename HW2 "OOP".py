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


print(f"Simba is instance of Animals:", isinstance(simba, Animals))
print(f"Bobik is instance of Animals:", isinstance(bobik, Animals))
print(f"Murka is instance of Animals:", isinstance(murka, Animals))
print(f"Felix is instance of Animals:", isinstance(felix, Animals))
print(f"Tony is instance of Animals:", isinstance(tony, Animals))


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


abas = Centaur("Abas")
print(abas.hunt(), abas.cook(), abas.sleep(), abas.work(), abas.study(), abas.eat(), sep='\n')

# Task 2a

print("Task 2a")


class Person:
    def __init__(self):
        left_arm = Arm('Left arm do some action')
        right_arm = Arm('Right arm do some action')
        self.arms = [left_arm, right_arm]


class Arm:
    def __init__(self, some):
        self.some = some


person = Person()

for arm in person.arms:
    print(arm.some)


# Task 2b

print("Task 2b")


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, screen_type):
        self.screen_type = screen_type


diagonal = Screen("Screen has diagonal 5,5")
phone = CellPhone(diagonal)
print(phone.screen.screen_type)


# Task 3

print("Task 3")


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.list = [self.name, self.last_name, self.phone_number, self.address, self.email,
                     self.birthday, self.age, self.sex]

    def __str__(self):
        return str(self.list)


profile1 = Profile(name="Robert", last_name="Nolan", phone_number="0974527134", address="New York",
                   email="robert123@gmail.com", birthday="13.04.1987", age="34", sex="male")

print(profile1)

# Task 4

print("Task 4")

from abc import abstractmethod, ABC


class LaptopABS(ABC):

    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass

    @abstractmethod
    def webcam(self):
        pass

    @abstractmethod
    def ports(self):
        pass

    @abstractmethod
    def dynamics(self):
        pass


class HPLaptop(LaptopABS):
    def screen(self):
        print("The screen has size 17 inch")
        
    def keyboard(self):
        print("The keyboard has a backlight")
        
    def touchpad(self):
        print("The touchpad has two buttons")
        
    def webcam(self):
        print("The webcam has fullHD resolution")
        
    def ports(self):
        print("Laptop has 3 ports")
        
    def dynamics(self):
        print("Laptop has 2 dynamics")


hp = HPLaptop()
print(hp.screen())
print(hp.dynamics())
print(hp.ports())
print(hp.webcam())
print(hp.keyboard())
print(hp.touchpad())
