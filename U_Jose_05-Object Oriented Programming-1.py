# print(type([]))
# print(type({}))
# print(type(()))
# print(type(1))
# print(type('10'))
# print(type(1.2))

# class Dog:
#     def __init__(self, breed, color):
#         self.breed = breed
#         self.color = color
#
#
# sam = Dog(breed='Lab', color='white')
# frank = Dog(breed='Huskie', color='white')
#
# print(f' sam is {sam.color} {sam.breed}')

# mylist = [1, 2, 3]
#
# myset = set()
#
# type(myset)
#
#
# class Dog():
#
#     species = 'mammal'
#
#     def __init__(self, breed, name, spots):
#         self.breed = breed
#         self.name = name
#         self.spots = spots
#
#
#
# my_dog = Dog(breed='Lab', name='Sammy', spots=False)
# my_cat = Dog(breed='',name='',spots='')
# print(type(my_dog))
# my_dog.species = 'POP'
# print(my_dog.breed)
# print(my_dog.name)
# print(my_dog.spots)
# print(my_dog.species)

# for i in dir(my_dog):
#     if not i.startswith('__'):
#         print(i)


# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius=3):
#         self.radius = radius
#         self.area = radius*radius*Circle.pi
#
#     def set_radius(self, newradius):
#         self.radius = newradius
#
#     # def set_radius2(self, radius2= 2):
#     #     self.radius2 = radius2
#
#     def Circumference(self):
#         return self.radius * 2 * Circle.pi
#
#
# c = Circle()
#
# print(c.Circumference())
# c.set_radius(6)
# print(c.Circumference())
# print(c.area)

#
# class Animal:
#     def __init__(self):
#         print('Animal created')
#     def who_am_i(self):
#         print('I am an animal')
#     def eat(self):
#         print('I am eating')
#
# myanimal = Animal()
#
#
# myanimal.eat()
# myanimal.who_am_i()
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print('Dog crated')
#     def who_am_i(self):
#         print('I am a dog')
#     def bark(self):
#         print('WOOF!')
# mydog = Dog()
#
# mydog.who_am_i()
#
# mydog.bark()

################ POLYMORPHISM ##############################

# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return (self.name + ' says woof')
#
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return(self.name + ' says meow')
#
# niko = Dog('niko')
#
# felix = Cat('felix')
#
# print(niko.speak())
# print(felix.speak())
#
#
# for pet in [niko, felix]:
#     print(pet.speak())
#     print(type(pet))
#
# def pet_speak(pet):
#     print(pet.speak())
#
# pet_speak(niko)
# pet_speak(felix)
#
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         raise NotImplementedError('Subclass must implement this abstract method')
#
#
# class Dog2(Animal):
#
#     def speak(self):
#         return self.name + ' says woof'
#
#
# class Cat2(Animal):
#
#     def speak(self):
#         return self.name + ' says meow'
#
# bob = Dog2('bob')
# bory = Cat2('bory')
#
# print(bob.speak())
# print(bory.speak())
#
#
# for pet in [niko, felix, bob, bory]:
#     print(pet.speak()+'2')
#     print(type(pet))


# mylist = [1,2,3]
# len(mylist)
#
# class Sample():
#     pass
#
# mysample = Sample()
#
# print(mysample)
# print(len(mysample))


# class Circl:
#     pi = 3.14
#
#     def __init__(self, radius):
#         self.radius = radius
#         self.area = radius * radius * Circl.pi
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#         self.area = new_radius * new_radius * Circl.pi
#
#     def getCircumference(self):
#         return self.radius * 2 * Circl.pi
#
#
# c = Circl(5)
#
# print(c.area)
# print(c.radius)
# print(c.getCircumference())
#
# c.set_radius(10)
#
# print(c.area)
# print(c.radius)
# print(c.getCircumference())
#
# ## Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
# class Line:
#     def __init__(self, coor1, coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
#
#     def distance(self):
#        return ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**0.5
#
#     def slope(self):
#         return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
#
#
# coordinate1 = (3, 2)
# coordinate2 = (8, 10)
# li = Line(coordinate1, coordinate2)
#
# print(li.distance())
# print(li.slope())
#
#
# class Cylinder:
#     pi = 3.14
#     def __init__(self, height=1,radius=1):
#         self.height = height
#         self.radius = radius
#
#     def volume(self):
#         return self.radius**2 * self.pi * self.height
#
#     def Area(self):
#         return 2*self.radius * self.pi * (self.height+self.radius)
#
#
# c = Cylinder(2, 3)
#
# print(c.volume())
# print(c.Area())


class Account:
    def __init__(self, owner, balance, password=1111):
        self.owner = owner
        self.balance = balance
        self.password = password

    def deposit(self):
        dep_amount = int(input('Please, enter the amount of your deposit: '))
        self.balance += dep_amount
        print(f' You have deposited {dep_amount}rub. Your balance is {self.balance}rub.')
        return self.balance

    def withdraw(self):
        dep_amount = int(input('Please, enter the amount of your withdraw: '))
        self.balance -= dep_amount
        print(f' You have withdrawn {dep_amount}rub. Your balance is {self.balance}rub.')
        return self.balance

    def checking_balance(self):
        if self.balance > 0:
            return True
        else:
            return False

    def finish(self):
        finish_operations = input(f'{self.owner}, do you wanna finish operations with your account, y or n:')
        if finish_operations == 'y':
            return True
        else:
            return False



acct1 = Account('Ilya', 100)

print('Welcome to the Bank')

while True:
    name = input('Please, enter name: ')
    password = input('Please, enter password: ')
    while True:
        if name == acct1.owner and password == acct1.password:
            operation = True
        else:
            operation = False


print('Account owner: ', acct1.owner, '\n'
      'Account balance:', acct1.balance)

acct1.deposit()
acct1.withdraw()