with open(".\dummy\dummy.txt", mode = 'a') as my_file:
    text = my_file.write("I am HAPPY!")
    print(text)     # it prints the no. of letters written into the file
    
    
with open("F:\Python\ZTM-Python\File IO\dummy\dummy.txt", mode = 'r') as my_file:
    print(my_file.read())
    
'''
we can give absolute path
or related path (wrt to the current folder)
../ means go back one folder
./ menas start from current folder

pathlib module: for windows, linex paths are different, so we can use this module so that our code works in all machines.
'''