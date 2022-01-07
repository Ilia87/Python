####  1 Write a function that computes the volume of a sphere given its radius.
# import math
#
# def vol(radius):
#     print(4 / 3 * math.pi * radius**3)
#
# vol(2)
############################################################################################


####  2  Write a function that checks whether a number is in a given range (inclusive of high and low)

# def ran_check(num,low,high):
#     ## array_low_high = []
#     ## for n in range(low, high+1):
#     ##     array_low_high.append(n)
#     if num in range(low, high+1):
#         print(f'{num} is in the range between {low} and {high}')
#     else:
#         print(f'{num} is NOT in the range between {low} and {high}')
#
#
# ran_check(6,2,5)
############################################################################################


####  3 Write a Python function that accepts a string
####    and calculates the number of upper case letters and lower case letters.

sample_string= 'Hello Mr. Rogers, how are you this fine Tuesday?'
#
# def up_low(string):
#     list_up = []
#     list_low = []
#     for l in string:
#         if l in (' ','?',',','.'):
#             pass
#         elif l.isupper():
#             list_up.append(l)
#         else:
#             list_low.append(l)
#     print(f'No. of Upper case characters : {len(list_up)}')
#     print(f'No. of Lower case Characters : {len(list_low)}')
#
#
# up_low(sample_string)

# def up_low_2(string):
#     lowercase = 0
#     uppercase = 0
#     other = 0
#
#     for l in string:
#         if l.isupper():
#             uppercase += 1
#         elif l.islower():
#             lowercase += 1
#         else:
#             other += 1
#     print(string)
#     print(f'No. of all case: {len(string)}')
#     print(f'No. of Upper case characters: {uppercase}')
#     print(f'No. of Lower case Characters: {lowercase}')
#     print(f'No. of other cases: {other}')


# up_low_2(sample_string)



############################################################################################


####  4 Write a Python function that takes a list and
####    returns a new list with unique elements of the first list.

sample_list = [3, 3, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
#
# def unique_list(array):
#     list_u = []
#     list_u.append(array[0])
#     for index in range(len(array)):
#         if array[index] not in (array[::index+1]):
#             list_u.append(array[index])
#     print(list_u)
#
#
# unique_list(sample_list)

# def unique_list_2(array):
#     search_unique = []
#     for num in array:
#         if num not in search_unique:
#             search_unique.append(num)
#     print(search_unique)
#
#
# unique_list_2(sample_list)


############################################################################################


####  5 Write a Python function to multiply all the numbers in a list
#
# list_sample_2 = [1, 2, 3, -4, 10]
#
# # result = list(map(lambda x: x * x,list_sample_2))
# # print(result)
#
# def multiply(array):
#     result = 1
#     for num in array:
#        result *= num
#     print(result)
#
# multiply(list_sample_2)

############################################################################################


####  5 Write a Python function that checks whether a word or phrase is palindrome or not.

# list_words = ['kcehc abc','madam','kayak','racecar','nurses run']
#
# def polindrom(words):
#     list_rev_text = []
#     for word in words:
#         list_rev = []
#         text = ''
#         for index_word in range(len(word)):
#             list_rev.append(word[len(word) - index_word-1])
#             text = ''.join(list_rev)
#         for l in word:
#             if l == ' ':
#                 text = " ".join(word.split()[::-1])
#         list_rev_text.append(text)
#     print(list_rev_text)
#
# polindrom_2(list_words)
#
# def polindrom_2(words):
#     list_rev_text = []
#     for word in words:
#         word = word.replace(' ', '')
#         print(word == word[::-1])
#
#
# def polindrom(words):


############################################################################################


####  6 Write a Python function to check whether a string is pangram or not.
#### (Assume the string passed in does not have any punctuation)


# for_example = 'The quick brown FOX jumps over the lazy dog'
# print(for_example.lower())
# def ispangram(string):
#     set_letter = set(list(map(chr, range(97, 123))))
#     set_string = set()
#     for l in string.lower():
#         if l == ' ':
#             pass
#         else:
#             set_string.add(l)
#     print(set_letter)
#     print(set_string)
#     print(set_letter.issubset(set_string))
# #
# #
# ispangram(for_example)
#
# def ispangram_2(string):
#     set_letter = set(list(map(chr, range(97, 123))))
#     string = string.lower()
#     string = string.replace(' ', '')
#     string = set(string)
#     print(string)
#     print(set_letter)
#     print(string == set_letter)
#
#
# ispangram_2(for_example)
