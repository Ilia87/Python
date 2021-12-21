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

def text_rev(text):
    list_text = []
    text_tmp = text.split(" ")
    for index in range(len(text_tmp)-1, -1, -1):
        list_text.append(text_tmp[index])
    for index1 in range(len(text_tmp)):
        list_text.append(index1)
    text_tmp2 = ' '.join(text.split(" ")[::-1])
    print(text_tmp)
    print(text_tmp2)
    print(list_text)

text_rev('I am home and it is great')