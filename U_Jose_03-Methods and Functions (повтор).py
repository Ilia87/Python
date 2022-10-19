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

def animal_crackers(text):
    words = [i for i in text.split(" ")]
    if words[0][0] == words[1][0]:
        print(True)
    else:
        print(False)

animal_crackers('fFWG Gdw')