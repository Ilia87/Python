# a = 100
# a = a + a
# b = 3.1
# print(a+a)
# print(type(a), type(b))
#
# print("I'm going")
# print('hi \tman')
#
# print(len('few           fw'))

# a = 'abcdefghijk'
# print(a)
# print(a[:3], ' a[:3] ')
# print(a[:-3], ' a[:-3] ')
# print(a[-3:], ' a[-3:] ')
# print(a[::3], ' a[::3] ')
# print(a[3::], ' a[3::] ')
# print(a[3:], ' a[3:] ')
# print(a[::2], ' a[::2]')
# print(a[::-1], ' a[::-1]')
# print(a[::-2], ' a[::-2]')
# print(a[:2], ' a[:2]')
# print(a[2:], ' a[2:]')
#
# b = 'tinker'
# print(b[1:4])
# print(b[-5:-2])

# c = 'Nice day'
# print(c)
# c = 'it was ' + c
# print(c)
# print(c[7:12])
# print(c[:6] + ' bad ' + c[12:])
# c=c[:6] + ' bad ' + c[12:]
# c=c*2
# print(c)

# c = 'The {v} {n} {d}'
# print(c.format(v='very', n='nice', d='day',))
#
# b = 'The {} {} {}'
# print(b.format('very', 'nice', 'day',))
#
# q= 100
# w = 45
# result = q/w
# print(result)

# x, y = input('your name: '), float(input('your age: '))
# print("I'm %s and my age is %d years old.\nHowever age is %5.4f" % (x, y, y))
# 
#
# old_list = [1, 2, 3, 4, 5, 6]
# print(old_list)
# print(len(old_list))
# print(old_list[0])
# new_list = old_list[:]
# new_list.append(7)
# print(new_list)
# new_list2 = new_list.copy()
# new_list2.pop(0)
# print(new_list2)
# print(old_list + new_list)
# big_list = old_list[:] + new_list.copy()
# print(big_list)
# big_list.sort()
# print(big_list)
# big_list.reverse()
# print(big_list)
# matrix = [old_list, new_list, new_list2, big_list]
# print(matrix)
# print(matrix[3])
# first_col = [row[0] for row in matrix]
# print(first_col[1:])

# Dictionaries

d = {'c1': ['a', 'b', 'c', 'd', 'e'], 'c2': [1, 2, 3, 4, 5], 'c3': {'c3_1': ['z', 'x']}}
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d['c3']['c3_1'][1])
d['c3']['c3_1'][1] = 'g'
print(d['c3']['c3_1'][1])
d['c3']['c3_1'][1].upper()
print(d['c3']['c3_1'][1])
d['c2'] += {'name'}
# d['c2']['name'] = {}

print(d)
print(d['c2'])
print(d.items())
list = list(d.items())
list1 = [1,1,2,2,3,4,5,6,1,1]
print(list1)
set(list1)
print(set(list1))
x=set(list1)
x.remove(2)
print(x)
