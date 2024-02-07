'''
Pure Function Have 2 Rules
1. For Same Input There Have To Same Output Everytime
2. Should Not Produce Any Side Effect
'''
def multiply_by2(li):
    new_li = []
    for item in li:
        new_li.append(item)
    return new_li

print(multiply_by2([5,6,8]))

'''
If we define 'new_li' outside the function, or print something inside the function, then it is no longer
a pure function, it would create side effect.
'''