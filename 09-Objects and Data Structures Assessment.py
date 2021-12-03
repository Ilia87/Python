# print(4*(6+5))
# print(4*6+5)
# print(type(3+1.5+5))
# print(9**2)
# print(9%2)
# print(9**0.5)
#
# s = 'hello'
# print(s[0:])
# print(s[1])
# print(s[::-1])
# print(s[-1])
# print(s[4])
# print(s[4:])
# print(s[::2])
#
# list = [0]
# list2 = list * 3
# print(list2)
#
# list3 = [1,2,[3,4,'hello']]
# print(list3[2])
# print(list3[2][2])
# list3[2].pop(2)
# print(list3)
# list3[2].append('goodbye')
# print(list3)

d = {'simple_key':'hello'}
print(d['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d3['k1'][0]['nest_key'][1] = 'hello'
print(d3['k1'][0]['nest_key'][1])
print(d3.keys())
d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d4['k1'][2]['k2'][1]['tough'][2] = 'hello'
print(d4['k1'][2]['k2'][1]['tough'][2])
