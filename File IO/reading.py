my_file = open('test.txt')
print(my_file)
print(my_file.read())

print(my_file.read())   # this won't be printing anything. because the cursor is at the end of the file.

print("Seek 0")
my_file.seek(0)     # seek function reset the cursor to the initial position.

print(my_file.read())   # and so we can now read the file from the initial position till end.

print("Seek 0")
my_file.seek(0)

print(my_file.readline())   # this reads a line and stop the cursor
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

print("Seek 0")
my_file.seek(0)

print(my_file.readlines()) # this store all the lines in a list
print(my_file.readlines())

my_file.close() # this for colse the file