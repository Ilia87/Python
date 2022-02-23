# def add(n1, n2):
#     print(n1 + n2)
#
#
# print(add(10, '20'))


# try:
#     # Want to attempt this code
#     # may have an error
#     result = 10 + 10
# except:
#     print('hey it looks like you are not adding correctly')
# else:
#     print('Add went well')
#     print(result)
#
# # print(result)

# try:
#     f = open('testfile.txt', 'r')
#     f.write('Write a test line')
# # except TypeError:
# #     print('There was a type error!')
# # except OSError:
# #     print('Hey you have an OS Error')
# except:
#     print('All other exceptions!')
# finally:
#     print('I always run')

# def ask_for_int():
#     while True:
#         try:
#             result = int(input('Please provide number: '))
#         except:
#             print('That is not a number')
#             continue
#         else:
#             print('Yes, thank you')
#             break
#         finally:
#             print('I am going to ask you again! \n')
#
# ask_for_int()

# def sample():
#     try:
#         for i in ['a','b','c']:
#             print(i**2)
#     except:
#         print('some kind errors happened')
#
#
# sample()

# def sample1(x, y):
#     try:
#         print(x / y)
#     except ZeroDivisionError:
#         print('the second argument of a division or modulo operation is zero')
#     finally:
#         print(f'{int(x / (y+1))} is better. We added 1 to {y}')
#
#
# sample1(5,0)

# def ask():
#     ## we can use without waiting = True
#     waiting = True
#     while waiting:
#         try:
#             number = int(input('Input an integer: '))
#         except:
#             print('An error occurred! Please try again! \n')
#             continue
#         else:
#             print(f'Thank you, your number squared is:  {number**2}')
#             waiting = False
#             break
#         finally:
#             print('Finally, I executed!')
#
#
# ask()
import pylint
pylint.run_pylint()
a = 15
b = 2
print(a)
print(B)