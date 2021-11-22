# flag = True
# N = int(input('your first number: '))
# for i in range(N):
# 	x=int(input('your second number: '))
# 	flag= (x%10 == 0) or flag

# print(flag)

# x=int(input())
# if x % 2 == 0:
# 	print('yes')
# if x % 3 == 0:
# 	print('yes')

# x=int(input('your first number:' ))
# if x==1:
# 	print('yes1')
# if x==2:
# 	print('yes2')

# x=int(input('your number:' ))
# if x < 0:
# 	print('A')
# elif x < 5:
# 	print('B')
# elif x < 10:
# 	print('C')
# else:
# 	print('D')
# 	


# z = 0o4575154
# print (z)

# x=1
# while x < 24:

# 	print(x, end=',')
# 	x *= 2
# for i in range(20, 10, -2):
#    print(i, end=',')

# def max2(x, y):
# 	if x > y:
# 		return x
# 	return y
# def max6(x,y,z,a,b,c):
# 	return max2(x,max2(y, max2(z, max2(a, max2(b, c)))))
# print(max6(5,8,1222,525252,45,1))

# def hello_separated(name="World", separator="-"):
#     print("Hello", name, sep=separator)
#
#
# hello_separated(separator="***",
#                 name="Ilya")
#
# def is_simple_number(x):
#     divisor = 2
#     while divisor < x:
#         if x % divisor == 0:
#             return False
#         divisor += 1
#     return True

# print(is_simple_number(2727))

# A = [i*i for i in range (1000)]
# print(A)
# A = [0] * 1000
# top = 0
# x = int(input('введите верхнее значение: '))
# while x != 0:
#     A[top] = x
#     top += 1
#     x = int(input('one more: '))
# for k in range(4, -1, -1):
#     print(A[k])

# for x in A:
#     # # print (x)
#     # x=x*x
#     print(x)
# print(A)
# for k in range(5):
#     A[k] = A[k] * A[k]
# print(A)

# A = [i for i in range(10)]
# print(A, end=" ")
# n = int(input('число: '))
# A = [0] * n
# B = [0] * n
# for k in range(n):
#     A[k] = int(input('число2: '))
# print(A)
# for k in range(n):
#     B[k]=A[k]
# print('сделали копию массива: ', B)
# C = list(A)
# print('one more variant to copy ')

def array_search(A: list, N: int, x: int):
    """searching value of X in list A
    from 0 to N-1 included.
    Return index of X in list A.
    Or -1, if it doesn't exist.
    if there are some aqual number then return first
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1

def test_array_search():
    A1 = [1,5565,4677,4,456]
    m = array_search(A1, 5, 555)
    if m == 1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 4:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    A3 = [10, 20, 30, 40, 50]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

test_array_search()
