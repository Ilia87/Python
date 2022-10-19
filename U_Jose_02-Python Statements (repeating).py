##Use for, .split(), and if to create a Statement that will print out words that start with 's':

# st = 'Print only the words that start with s in this sentence'
# lst = []
# lsts = []
# for i in st.split(" "):
#    lst.append(i)
# for w in lst:
#     if "s" in w[0]:
#         lsts.append(w)
#
# print(lst)
# print(lsts)
#
# # Recomendation
# for word in st.split(" "):
#     if word[0] == "s":
#         print(word)

# # Use range() to print all the even numbers from 0 to 10.
#
# lst_even = [n for n in range(0, 12, 1) if n % 2 == 0]
# # for n in range(0, 12, 2):
# print(lst_even)

## Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

# lst_div3 = [n for n in range(50) if n % 3 == 0]
# print(lst_div3)

## Go through the string below and if the length of a word is even print "even!"

# st = 'Print every word in this sentence that has an even number of letters'
#
# lst_word_even = [w for w in st.split(" ") if len(w) % 2 == 0]
# print(lst_word_even)
# lst_even = [len(w) for w in lst_word_even]
# print(lst_even)
#
# lst_combo = []
# n = 0
# for w in lst_word_even:
#     w_n = str(lst_even[n])
#     w = w + "_" + w_n
#     lst_combo.append(w)
#     n += 1
# print(lst_combo)

# # Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
#
# lst = ["Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else "FizzBuzz" if n % 5 == 0 and n % 3 == 0 else n for n in
#        range(101) if n % 3 == 0 or n % 5 == 0 ]
# print(lst)

# # //Use List Comprehension to create a list of the first letters of every word in the string below:
#
# st = 'Create a list of the first letters of every word in this string'
#
# lst = [n[0] for n in st.split(" ")]
# print(lst)

import random

num = random.randint(1, 100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = [0]

while True:
    guess = int(input("I think the number betweуn 1 and 100. Wnat do you think "))
    if guess < 1 or guess > 100:
        print(f'the {guess} out of range')
        continue
    if num == guess:
        print(f'you won, you spent {len(guesses)}')
        break
    guesses.append(guess)
    if guesses[-2]:
        if abs(num - guesses[-2]) < abs(num - guess):
            print('дальше')
        else:
            print('жарче')
    else:
        if abs(guess - num) >= 10:
            print('Cold')
        else:
            print('Warm')

