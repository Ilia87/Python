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


def cap_letters(word):
    lst_letters = list(word)
    lst_cap = ''
    for l in lst_letters:
        if lst_letters.index(l) == 0 or lst_letters.index(l) == 3:
            lst_cap += l.upper()
        elif lst_letters.index(l) != 0 or lst_letters.index(l) != 3:
            lst_cap += l
    print(lst_cap)
    for pos, letter in enumerate(lst_letters):
        print(f"{letter}: {pos}")
    letter_enum = enumerate(lst_letters)
    print(list(letter_enum))
    lst_cap_second = ''
    for i in letter_enum:
        for n in range(len(i)):
            if i[n][0] == 0:
                lst_cap_second += i[n][1].upper()
            else:
                lst_cap_second += i[n][1]
        print(lst_cap_second)


cap_letters('макдоналдм')