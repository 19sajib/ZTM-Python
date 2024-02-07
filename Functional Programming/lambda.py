import functools

my_list = [1,2,3,4,5]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(functools.reduce(lambda acc,item: item+acc, my_list))

'''
syntax:
lambda param: action(param)
it automatically returns the action taken,
it do not have any name, doesn't get stored in the memory.
and so used only once.
and behaves exactly like a function.
'''

# Square
my_list = [5, 4, 3]

print(list(map(lambda item: item*item, my_list)))

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -2)]

a.sort(key=lambda x: x[1])
print(a)

a = [(0,2),(4,4),(10,-1),(5,3)]

a.sort(key=lambda x:x[1], reverse=False)
print(a)