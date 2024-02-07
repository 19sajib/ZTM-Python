# we can stop the program by raising our own errors.

try:
    age = int(input("age: "))
    age = 10/age
    raise ValueError("Ending the program")
    # raise Exception("quit")

except ValueError:
    print("Please enter a no.")
    
# raise exception
print("Hello!!!!")
# raise TypeError("yo")
raise Exception("Any message ")
print("bye")
