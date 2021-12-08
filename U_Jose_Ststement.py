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


list1 = []
st = 'Print only the words that start with s in this sentence'
for i in st.split(" "):
    list1.append(i)
print(list1)
for w in list1:
    if "s" in w[0]:
        print(w[::-1])


     # if "s" in i[0]:
     #     print(i)

