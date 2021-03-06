"""
Two types of functions. Ones that are builtin to python, and others that you define
To define a function, specify def and give it a name and action:
"""
def greeting():
    print('Hello')

# You can define functions inside of functions if you want
    def slang():
        print('wuddup')
# Then you can call the functions that you made. AKA invoking the function.
    slang()
greeting()

# Add arguments and assign values to them in the function
def func(x, y, z=None):
    print('Run', x, y)
# Run a return on the values:
    return x * y, x / y
# Specify the values for x and y:
print(func(5, 6))

# Notice the default value associated with z is None. This is an optional parameter. If you want override the default value later you can.
def func2(x, y, z=None):
    print('Run2', x, y, z)
    return x * y, x /y

r1, r2 = func2(5, 6)
print(r1, r2)
# The same again but with the optional parameter set.
def func2(x, y, z=None):
    print('Run2', x, y, z)
    return x * y, x /y

r1, r2 = func2(5, 6, 7)
print(r1, r2)

# Functions are objects that can be passed around like variables. You can define a function and call it later on in the code.
def funct(x):
        def funct2():
            print(x)
        return funct2

# Then call it later. Here we called it later with value 3 for funct and nothing for funct2.
print(funct(3)())
# Or
x = funct(3)
x() 

# Unpack Operators
# Defining a function to use with unpack operators.
def func():
    pass

x = [1,54,5345,295,683345,3756,2854]
y = [5,234,56,3221,675,345]

print(x)
# Unpack x. Take the values from the list and pass them to print as individual values.
print(*x)

print(y)
# Unpack y
print(*y)

# Another example of the unpack operator
def func(x, y):
    print(x, y)
# Pass a few pairs to the function
pairs = [(1,2), (3,4)]
# Then unpack them. takes 1,2 and 3,4 and unpacks them then passes the values to func
for pair in pairs:
    func(*pair)
# pass a dictionary to func as an argument
func(**{'x': 2, 'y':5})
# double asterics ** are used for dictionaries, single asterics * used for tuples and lists

# *args (arguments) and **kwargs(keyword arguments)
# Allows you to pass an unlimited amount of arguments and keyword arguments.
def func(*args, **kwargs):
# When your print args and kwargs you will get a tuple that has all of the positional arguments (args) and all of the keyword arguments (kwargs)
    print(args, kwargs)
# Unpack args
    print(*args)
func(1,2,23,4,55,3,46,one=0, two=2004)


# Defining scope and global
x = 'Bill'

def func(name):
# Attemptint to change x to name here will not work, since it was assigned earlier as a global variable.
    x = name

print(x)
func('changed')
print(x)

















"""
Builtins

type()
Type is used to show what type specified data is
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""
x = 20
print (type(x))

x = ["apple, cherry, banana"]
print(type(x))

x = "8k0si0n2"
print(type(x))

# input()
# The input funcion is used to accept user input
# You can assign their input to a variable like so:
name = input('who are you? ')
print("welcome", name)

# open()
# tell python to work with a specific file and what we want to do with the file
# open() returns a "file handle" - a variable used to perform operations on the file.

# Using open()
# # handle=open(filename, mode)
# fhand = open('mbox.txt', 'r')
# print(fhand)
