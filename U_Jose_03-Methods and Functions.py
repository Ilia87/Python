# def get_res(a, b):
#     print(a * b)
#     return (a * b)
#
# get_res(15, 4)
# tmp = get_res(15, 10)
# print(type(tmp))
# print(tmp + tmp * tmp)
#
# def check_num(number):
#     return number % 2 == 0
#     print(number % 2 == 0)
#
# print (check_num(45))

# def check_even(num_list):
#     list1 = []
#     for num in num_list:
#         if num % 2 == 0:
#             list1.append(num)
#         else:
#             pass
#     print(list1)
#     return list1
#
# # check_even([1,45,64,64,213,7,46,13,6,4,63,6,6,654,654,])
#
# list_tup1 = [('Abby',100),('Billy',400),('Cassie',800)]
#
# def tup(list_tup):
#     salary_max = 0
#     name_emp = ''
#     for emp,salary in list_tup:
#         if salary > salary_max:
#             salary_max = salary
#             name_emp = emp
#         else:
#             pass
#     print((name_emp, salary_max))
#     return (name_emp, salary_max)
#
# tup(list_tup1)

# from random import shuffle
#
# # Initial List
# mylist = ['8','O','8']
#
# def shuffle_list(mylist):
#     shuffle(mylist)
#
#     return mylist
#
# def player_guess():
#     guess = ''
#     while guess not in ['0', '1', '2']:
#         guess = input("Please write 0, 1, 2:  ")
#
#     return int(guess)
#
#
# def check_guess(mylist, guess):
#     if mylist[guess] == 'O':
#         print('Correct Guess!')
#     else:
#         print('Wrong! Better luck next time')
#         print(mylist)
#
#
# mix = shuffle_list(mylist)
# gue = player_guess()
# check_guess(mix, gue)

# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and  b % 2 == 0:
#         if a > b:
#             print(b)
#             return b
#         else:
#             print(a)
#             return a
#     else:
#         if a < b:
#             print(b)
#             return b
#         else:
#             print(a)
#             return a
# lesser_of_two_evens(10,810)

# def animal(text):
#     list_text = list(text.split(" "))
#     print (list_text[0][0] == list_text[1][0])
#     return list_text[0][0] == list_text[1][0]
#     #     print('True')
#     #     return "True"
#     # else:
#     #     print('False')
#     #     return "False"
#
# animal("robot rak")
#
# def check(a,b):
#     print (a == 20 or b == 20 or a+b == 20)
#     return a == 20 or b == 20 or a+b == 20
#     # if a == 20 or b == 20 or a+b == 20:
#     #     print('True')
#     #     return "True"
#     # else:
#     #     print('False')
#     #     return "False"
#
# check(55555555555555555,20)

# def old_macdonald(name):
# new_name = ''
# list_mac = list(name)
# list_mac.pop(3)
# list_mac.insert(3,"D")
# list_mac.pop(0)
# list_mac.insert(0,"M")
# for l in list_mac:
#     new_name +=l
# print(new_name)

# def old_macdonald(name):
#     if len(name)>4:
#         print(name[:3].capitalize() + name[3:].capitalize())
#         return name[:3].capitalize()
#     else:
#         print("it is too short")
#
#
# old_macdonald('macdonald')

# def rev_t(text):
#     text = "".join(reversed(text))
#     print(text)
# rev_t('We are ready')
#
# def rev_t1(text1):
#     text_list = list(text1.split(" "))
#     text_list.reverse()
#     print(' '.join(text_list))
# rev_t1('We are ready')
#
# def rev_t2(text2):
#     text2 = " ".join(text2.split()[::-1])
#     print(text2)
# rev_t2('We are ready')
# #
# def almost_there(n):
#     print (n > 10 and n < 100 or n>200)
#     print((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
#
# almost_there(209)

# def has_33(nums):
#     list_n = []
#     for n in range(1, len(nums)+1):
#         list_n.append(n)
#     # print(list_n)
#     lisrd = []
#     for i in nums:
#         lisrd.append(i == 3 and nums[nums[i]-1] == 1 or i == 3 and nums[nums[i]+1] == 1)
#     # print(lisrd)
#     # print(nums)
#     list_f = list(zip(list_n, nums, lisrd))
#     # print(list_f)
#     for i0, i1, i2 in  list_f:
#         print(f'в проверке № {i0}, число {i1} и вот результат {i2}')
#
# gu = [1, 3, 1, 3, 1, 7, 1, 3, 6, 7, 1, 3, 3, 1, 3, 1, 6, 7, 1, 3, 3, 1, 6, 7, 9]
#
# def has_3(nyms):
#     for i in range(0, len(nyms)-1):
#         # print(nyms[i:i+1] == [3,3] or nyms[i-1:i] == [3,3])
#         if nyms[i:i + 2] == [3, 3]:
#             print(True)
#         print(False)
#
# has_33(gu)
# has_3(gu)

# gu = [(1, 3, 1, 3, 1, 7, 1, 3, 6, 7, 1, 3, 3, 1, 3, 1, 6, 7, 1, 3, 3, 1, 6, 7, 9)]
# def myfunc(*args):
#     output = []
#     # out = [item for n1 in args for item in n1]
#     for n in args:
#         if n % 2 == 0:
#             output.append(n)
#         else:
#             pass
#     print(output)
#     return output
#
# myfunc(1, 3, 1, 3, 1, 7, 1, 3, 6, 7, 1, 3, 3, 1, 3, 1, 6, 7, 1, 3, 3, 1, 6, 7, 9)

# name = 'anthropomorphism'

#
# def my_func(st):
#     new = []
#     for index in range(len(st)):
#         if index % 2 == 0:
#             new.append(st[index].lower())
#         else:
#             new.append(st[index].upper())
#     word = ''.join(new)
#     print(word)
#
# my_func(name)

# name = 'anthropomorphism'

# def my_func(word):
#     list_word = []
#     for index in range(0,len(word)):
#         if index % 2 == 0:
#             list_word.append(word[index].lower())
#         else:
#             list_word.append(word[index].upper())
#     new_word = ''
#     for l in list_word:
#         new_word += l
#     return (new_word)
#
# my_func(name)

# Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Check
# master_yoda('I am home')
# Check
# master_yoda('We are ready')

# def text_rev(text):
#     list_text = []
#     text_tmp = text.split(" ")
#     for index in range(len(text_tmp) - 1, -1, -1):
#         list_text.append(text_tmp[index])
#         text_r = ' '.join(list_text)
#     # for index1 in range(len(text_tmp)):
#     #     list_text.append(index1)
#     text_tmp2 = ' '.join(text.split(" ")[::-1])
#     print(text_tmp)
#     print(text_tmp2)
#     print(list_text)
#     print(text_r)
#
#
# text_rev('I am home and it is great')

# def almost_there(n):
#     print(10 < n < 100 or n > 200)
# almost_there(201)

# list_c = [1, 3, 1, 3, 1, 7, 1, 3, 6, 7, 1, 3, 3, 3, 1, 3, 1, 6, 7, 1, 3, 3, 1, 6, 7, 9]

# def has_33(list_1):
#     list_number = []
#     list_check = []
#     for index in range(len(list_1)):
#         list_check.append(list_1[index] == list_1[index - 1] == list_1[index + 1] == 3)
#         list_number.append(index)
#     tuple_finish = list(zip(list_number,list_1, list_check))
#     # print(tuple_finish)
#     for i0, i1, i2, in tuple_finish:
#         print(f'checking #{i0} for number {i1} is {i2}')
#
#
# has_33(list_c)
#
# def paper_doll(word):
#     list_word=[]
#     for l in word:
#         list_word.append(l*3)
#     word_doll1 = ''.join(list_word) # Using .join() method
#     word_doll2 = ''.join(map(str,list_word)) # Use map() method for mapping str (for converting elements in list to string) with given iterator, the list.
#     word_doll3 = ''.join([str(le) for le in list_word]) # Using list comprehension
#     print(list_word)
#     print(word_doll1)
#     print(word_doll2)
#     print(word_doll3)
#
# paper_doll('Hello')


# tup1 = (5,6,7)
# tup2 = (9,9,9)
# tup3 = (9,9,11)
# tup4 = (9,50,11)
# def blackjack(integers):
#     if sum(integers)<=21:
#         print(sum(integers))
#     elif sum (integers) <= 31 and integers[0] == 11 or  integers[1] == 11 or  integers[2] == 11:
#         print(sum(integers) - 10)
#     else:
#         print('BUST')
#
# blackjack(tup1)
# blackjack(tup2)
# blackjack(tup3)
# blackjack(tup4)
#
# def summer_69(array):
#     list_array = []
#     for n in array:
#         if n <> 6

# t = 'Pilaf'
# def plof(text):
#     text1 = text.capitalize()[::-1]
#     print(text1)
# # plof(t)
#
# list_1 = [4, 5, 6, 7, 8, 9, 45, 11, 6, 5, 9, 11, 2]
#
# def sum_69(array):
#     array_n = []
#     array_i = []
#     for index, n in enumerate(array,0):
#         array_i.append(index)
#         array_n.append(n)
#     list_f = list(zip(array_i, array_n))
#     print(array_i)
#     print(array_n)
#     print(list_f)
#
# sum_69(list_1)
#
# def sum_69_1(array):
#     array_n = []
#     array_i = []
#     for index, n in enumerate(array, 0):
#         if n == 6:
#             continue
#         array_i.append(index)
#         array_n.append(n)
#         list_f1 = list(zip(array_i, array_n))
#     print(array_i)
#     print(array_n)
#     print(list_f1)
#
# sum_69_1(list_1)



#  Return the sum of the numbers in the array,
#  except ignore sections of numbers starting
#  with a 6 and extending to the next 9
#  (every 6 will be followed by at least one 9). Return 0 for no numbers.
# list_1 = [4, 5, 6, 7, 8, 9, 1, 11, 6, 5, 9, 11, 2]
# def sum_69(array):
#     list_sum =[]
#     list_not_sum = []
#     add = True
#     for n in array:
#         while add:
#             if n != 6:
#                 list_sum.append(n)
#                 break
#             else:
#                 list_not_sum.append(n)
#                 add = False
#                 break
#         while not add:
#             if n != 9:
#                 list_not_sum.append(n)
#                 break
#             else:
#                 add = True
#     print(list_sum)
#     print(list_not_sum)
#
# print(list_1)
# sum_69(list_1)

# SPY GAME: Write a function that takes in a list of integers
# and returns True if it contains 007 in order
# def spy_game(nums):
#     list_spy =[]
#     check = 1
#     for num in nums:
#         while check == 1:
#             if num != 0:
#                 break
#             else:
#                 list_spy.append(num)
#                 check = 2
#                 break
#         while check == 2:
#             if num != 0:
#                 break
#             else:
#                 list_spy.append(num)
#                 check = 3
#                 break
#         while check == 3:
#             if num != 7:
#                 break
#             else:
#                 list_spy.append(num)
#                 check = 4
#                 break
#     print(''.join(map(str, list_spy))=='007')
#
# def spy_game_solution(nums):
#     code = [0,0,7,'x']
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)
#             print(code)
#     print(len(code)==1)
#
#
#
# spy_game([1, 2, 4, 0, 0, 9, 5, 0, 2, 4, 0, 5, 5])
# spy_game([1, 7, 0, 2, 4, 0, 5, 7])
# spy_game([1, 7, 2, 8, 2, 4, 8, 5, 7, 0, 4, 5, 0,0,7])
#
# spy_game_solution([1, 2, 4, 0, 0, 9, 5, 0, 2, 4, 0, 'x', 5])
# spy_game_solution([1, 7, 0, 2, 4, 0, 5, 7])
# spy_game_solution([1, 7, 2, 8, 2, 4, 8, 5, 7, 0, 4, 5, 0,0,7])

# COUNT PRIMES: Write a function that returns the number of prime numbers
# that exist up to and including a given number

# def count_primes(one_num):
#     list_nums = []
#     list_nums_prime = []
#     count_el = 0
#     a = 2
#     for index in range(2,one_num):
#         list_nums.append(index)
#         if (a ** (index - 1)) % index == 1 and a % index != 0:
#             list_nums_prime.append(index)
#     for el in list_nums_prime:
#         count_el += 1
#
#
#     # print(list_nums)
#     print(list_nums_prime)
#     print(len(list_nums_prime))
#     print(count_el)
#
#
# count_primes(100)
from typing import Dict, Any


# def prime(one_num):
#     list_primes = []
#     list_check_x = []
#     list_check_y = []
#     x = 3
#     while x <= one_num:
#         list_check_x.append(x)
#         print(f'operator {x}')
#         for y in range(3, x, 2):
#             list_check_y.append(y)
#             if x % y == 0:
#                 x += 2
#                 list_check_y.clear()
#                 break
#         else:
#
#             print(f'checking {x} by list y: {list_check_y}')
#             list_check_y.clear()
#             list_primes.append(x)
#             x += 2
#
#     # print(list_check_x)
#     print(list_primes)
#     print(len(list_primes))

# prime(20)

# def print_big(word):
#     patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
#     alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
#     for letter in word:
#         for pattern in alphabet[letter.upper()]:
#             print(patterns[pattern])
#
#
# print_big('abcd')
#
# list_s = [1, 2, 4, 0, 0, 9, 5, 0, 2, 4, 0, 5, 5]
# #
# def map_test(num):
#     print(num**2)
#
#
# # list(map(map_test, list_s))
#
# for item in map(map_test, list_s):
#     print(item)

my_nums = [1, 2, 3, 4, 5]
# def square(num):
#     print(num % 2 == 0)
#
#
# list(filter(square, my_nums))

result = list(map(lambda x: x ** 2,my_nums))
print(result)

animals = ['dog', 'cat', 'parrot', 'rabbit']

print(list(map(lambda word: str.upper(word[0]) + str(word[1::]), animals)))

# print(upper_first)

# array = ['John','Cindy','Sarah','Kelly','Mike']
#
# def even(words):
#     if len(words) % 2 == 0:
#         print(words)
#     else:
#         print(words[0])
#
#
# list(map(even, array))
# list(filter(even, array))


