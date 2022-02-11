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

mylist = [1, 2, 3]

myset = set()

type(myset)


class Dog():

    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots



my_dog = Dog(breed='Lab', name='Sammy', spots=False)
my_cat = Dog(breed='',name='',spots='')
print(type(my_dog))
my_dog.species = 'POP'
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)

# for i in dir(my_dog):
#     if not i.startswith('__'):
#         print(i)

