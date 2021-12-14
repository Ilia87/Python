# list1 = [1,2,3,4,5,6,7,8,9,10]
#
# for i in list1:
#     # Check for even
#     if i == 6:
#         continue
#     elif i % 2 == 0:
#         print(i)
#     else:
#         print(f'Odd Number: {i}')

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_sum = 1
# for i in range(1,10,1):
#     list_sum2 = list_sum
#     list_sum = list_sum * i
#     print(f'list_sum = {list_sum}, list_sum2 = {list_sum2}')
#
# for i in 'Hello':
#     print('Hi')
#
# tup = (1,2,3)
# for i in tup:
#     print(i)
#
# list3 = [(1,2,3), (4,5,6), (7,8,9), (10,11,12)]
# print(len(list3))
#
# for a, b, c in list3:
#     print(a)
#     print(b)
#     print(c)

# d = {'k1': 1, 'k2': 2, 'k3': 3}
# for i in d.values():
#     for s in d.items():
#         print(f'{i} and {s}')


# x = 0
# y = 10
# z = 1
# while x <= y:
#     print(f'{x} from {y}')
#     with open(f'C:\\Users\\Ilia_Vekkerle\\Documents\\{x} from {y}.txt', mode='w+') as f:
#         f.write(f'{x} from {y}')
#         # f.write(f'{list(map(chr, range(1, 250)))}')
#     if x == y:
#         print('it is the end')
#         with open(f'C:\\Users\\Ilia_Vekkerle\\Documents\\it is the end {x} from {y}.txt', mode='w+') as f:
#             f.write(f'it is the end{x} from {y}')
#     else:
#         print(f'next value is {x+z}')
#     x += z

# index_count = 0
# word = 'Vekkerle'
# for letter in word:
#     print(f'at index {index_count} the letter is {letter}')
#     index_count += 1
# #
# for i,l in enumerate(word):
#     print(f'{i} is {l}')
#
# list1 = list(range(1,27,1))
# list2 = list(map(chr, range(ord('a'), ord('z')+1)))
# list3 = list(map(chr, range(ord('а'), ord('я')+1)))
# #
# #
# for i in zip(list1, list2, list3):
#     print(i)
# print(list(zip(list1, list2, list3)))

# list1 = list(range(1,101,1))
# print(min(list1))
# print(max(list1))
#
# from random import shuffle
# shuffle(list1)
# print(list1)

# Statements Assessment Test

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
# list1 = []
# st = 'Print only the words that start with s in this sentence'
# for i in st.split(" "):
#     list1.append(i)
# print(list1)
# for w in list1:
#     if "s" in w[0]:
#         print(w[::-1])
# if "s" in i[0]:
#     print(i)

# st2 = 'Print only the words that start with s in this sentence'
# list2 = []
# for word in st2[::-1].split(" "):
#     if word[0].lower() == 's':
#         print(word)
#         list2.append(word)
# print(list2)
# print(list2[::-1])

# Use range() to print all the even numbers from 0 to 10.
# list1 = []
# for i in range(1,11,1):
#     list1.append(i)
# print(list1)


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# list2 = [i for i in range(1,51,1) if i % 3==0]
# print(list2)

#  Go through the string below and if the length of a word is even print "even!"
# st = 'Print every word in this sentence that has an even number of letters'
# for l in st.split(" "):
#     if len(l) % 2 == 0:
#         print(l)


# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# list1 = []
# for i in range(1, 101, 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#         list1.append("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#         list1.append("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#         list1.append("Buzz")
#     elif i % 2 == 0:
#         print(i)
# print(list1)

#  Use List Comprehension to create a list of the first letters of every word in the string below:

# st = 'Create a list of the first letters of every word in this string'
# list1 = [l[0] for l in st.split(" ")]
# print(list1)
#
#
# def reverse_string3(s):
#     chars = list(s)
#     for i in range(len(s) // 2):
#         tmp = chars[i]
#         chars[i] = chars[len(s) - i - 1]
#         chars[len(s) - i - 1] = tmp
#     return ''.join(chars)
#
#
# data = reverse_string3(st)
# print(data)  # 'OBRUT'

import random

num = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = [0]

while True:

    # we can copy the code from above to take an input
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    # here we compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break

    # if guess is incorrect, add guess to the list
    guesses.append(guess)

    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section

    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')

