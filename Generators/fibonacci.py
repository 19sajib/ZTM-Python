# Using list
def fib(num):
    a = 0
    b= 1
    li=[]
    for i in range(num):
        li.append(a)
        temp = a
        a = b
        b = temp + b
    print(li)

num = int(input("Enter a number: "))
fib(num)

# Using range
def fib(number):
    n1 = 0
    n2 = 1
    for i in range(number):
        yield n1
        temp = n1
        n1 = n2
        n2 = temp + n2


for x in fib(100):
    print(x)