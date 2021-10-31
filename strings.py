# Strings
# Using the type function when combined with print will show the class or type of the variable.
hello = 'hello'
print(type(hello))
#String Methods
# String Methods are operations you can perform on a string that will change the output displayed based on the method specified
hello = 'hello'
print(hello.upper())
print(hello.lower())
print(hello.capitalize())
# Look for a specified string within a string and count the matching occurances.
print(hello.count('ll'))
# Be aware here that lowercase letters do not equal uppercase letters
hello = 'heLLo World'
# count will show 0 here because there are no lower case ll or no match for ll.
print(hello.count('ll'))
# to get around this, modify prints output by converting the string to lowercase with the lower method.
print(hello.lower().count('ll'))
# String Multiplication and addition
x = 'hello'
y = 'Bill'
# Repeat a string by multiplying
print(x *10)
# Concatenate two strings
print(x + y)
