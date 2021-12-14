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
# check_even([1,45,64,64,213,7,46,13,6,4,63,6,6,654,654,])

list_tup1 = [('Abby',100),('Billy',400),('Cassie',800)]

def tup(list_tup):
    salary_max = 0
    name_emp = ''
    for emp,salary in list_tup:
        if salary > salary_max:
            salary_max = salary
            name_emp = emp
        else:
            pass
    print((name_emp, salary_max))
    return (name_emp, salary_max)

tup(list_tup1)

