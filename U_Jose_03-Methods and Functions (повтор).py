# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

# def check_even(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         if a < b:
#             return a
#         else:
#             return b
#     else:
#         if a < b:
#             return b
#         else:
#             return a
#
# print(check_even(2, 4))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

# def animal_crackers(text):
#      words = [i for i in text.split(" ")]
#     if words[0][0] == words[1][0]:
#         print(True)
#     else:
#         print(False)
#
# animal_crackers('GFWG Gdw')


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the
# integers is 20. If not, return False

# def sum(a, b):
#     if a + b == 20 or a == 20 or b == 20:
#         print(True)
#     else:
#         print(False)
#
# sum(3, 20)

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald


# def cap_letters(word):
#     lst_letters = list(word)
#     lst_cap = ''
#     for index, l in enumerate(lst_letters):
#         if index == 0 or index == 3:
#             lst_cap += l.upper()
#         else:
#             lst_cap += l
#     print(lst_cap)
#
# cap_letters('макдоналдм')


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# # master_yoda('I am home') --> 'home am I'
# # master_yoda('We are ready') --> 'ready are We'

def master_yoda_1(text):
    lst_text = list(text.split(" "))
    lst_text.reverse()
    str_text = " ".join(lst_text)
    print(str_text)
def master_yoda_2(text):
    lst_text = list(text.split(" "))
    str_text = " ".join(reversed(lst_text))
    print(str_text)

def master_yoda_3(text):
    lst_text = list(text.split(" "))
    str_text = " ".join(lst_text[::-1])
    print(str_text)

def master_yoda_4(text):
    lst_text = list(text.split(" "))
    str_text = ''
    for n in range(len(lst_text)-1, -1, -1):
        str_text += lst_text[n]
        str_text += " "
    print(str_text)

def master_yoda_5(text):
    lst_text = list(text.split(" "))
    lst_text_rev = []
    for n in range(len(lst_text)-1, -1, -1):
        lst_text_rev.append(lst_text[n])
    str_text = " ".join(lst_text_rev)
    print(str_text)

def master_yoda_6(text):
    lst_text = list(text.split(" "))        

def master_yoda_6_tmp(lst_text):
    if len(lst_text) == 1:
        return lst_text
    else:
        return str(lst_text[-1]) + " " + str(master_yoda_6_tmp(lst_text[:-1]))



example = 'Я накидала на тебя волос, как мой кот на меня кидает'
master_yoda_1(example)
master_yoda_2(example)
master_yoda_3(example)
master_yoda_4(example)
master_yoda_5(example)
master_yoda_6(example)
example2 = ['Я', 'накидала', 'на', 'тебя', 'волос,', 'как', 'мой', 'кот', 'на', 'меня','кидает']
master_yoda_6_tmp(example)
