def only_even(item):
    return item % 2 == 0

my_list = [5,8,9,2,5,6,98,56,62]

print(filter(only_even, my_list))  
print(list(filter(only_even, my_list))) 
print(list(map(only_even, my_list))) 
print(my_list)

'''
since that filter is not modifying anything, and creating a new list. 
it is also using separate data and function to work upon them.
it's a nice concept of Functional programming and pure function.
'''