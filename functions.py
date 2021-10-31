# Two types of functions. Ones that are builtin to python, and others that you define
# To define a function, specify def and give it a name and action:
def greeting():
    print('Hello')

# You can define functions inside of functions if you want
    def slang():
        print('wuddup')
# Then you can call the functions that you made
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