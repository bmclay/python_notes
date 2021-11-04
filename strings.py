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

# String Format
# We cannot combine strings and numbers like this:
# age = 36
# txt = "My name is John, I am " + age
# print(txt)
# But we can like this, using the format method.
age = 36
txt = "My name is Bill, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 30
itemno = 5670
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 

# The escape character \ and the newline character \n 
print("\nMy name is \"Kid\"... \n\nKid ROCK!")
# \n is the newline character
print("\n") 

'''
Other escape characters
\' 	Single Quote 	
\\ 	Backslash 	
\n 	New Line 	
\r 	Carriage Return 	
\t 	Tab 	
\b 	Backspace 	
\f 	Form Feed 	
\ooo 	Octal value 	
\xhh 	Hex value
'''

# String Methods
'''
Builtin string methods
capitalize()          Converts the first character to upper case
casefold()            Converts string into lower case
center()	            Returns a centered string
count()	              Returns the number of times a specified value occurs in a string
encode()	            Returns an encoded version of the string
endswith()	          Returns true if the string ends with the specified value
expandtabs()	        Sets the tab size of the string
find()	              Searches the string for a specified value and returns the position of where it was found
format()	            Formats specified values in a string
format_map()	        Formats specified values in a string
index()	              Searches the string for a specified value and returns the position of where it was found
isalnum()	            Returns True if all characters in the string are alphanumeric
isalpha()	            Returns True if all characters in the string are in the alphabet
isdecimal()	          Returns True if all characters in the string are decimals
isdigit()	            Returns True if all characters in the string are digits
isidentifier()	      Returns True if the string is an identifier
islower()	            Returns True if all characters in the string are lower case
isnumeric()	          Returns True if all characters in the string are numeric
isprintable()	        Returns True if all characters in the string are printable
isspace()	            Returns True if all characters in the string are whitespaces
istitle() 	          Returns True if the string follows the rules of a title
isupper()	            Returns True if all characters in the string are upper case
join()	              Joins the elements of an iterable to the end of the string
ljust()	              Returns a left justified version of the string
lower()	              Converts a string into lower case
lstrip()	            Returns a left trim version of the string
maketrans()	          Returns a translation table to be used in translations
partition()	          Returns a tuple where the string is parted into three parts
replace()	            Returns a string where a specified value is replaced with a specified value
rfind()	              Searches the string for a specified value and returns the last position of where it was found
rindex()	            Searches the string for a specified value and returns the last position of where it was found
rjust()	              Returns a right justified version of the string
rpartition()	        Returns a tuple where the string is parted into three parts
rsplit()	            Splits the string at the specified separator, and returns a list
rstrip()	            Returns a right trim version of the string
split()	              Splits the string at the specified separator, and returns a list
splitlines()	        Splits the string at line breaks and returns a list
startswith()	        Returns true if the string starts with the specified value
strip()	              Returns a trimmed version of the string
swapcase()	          Swaps cases, lower case becomes upper case and vice versa
title()	              Converts the first character of each word to upper case
translate()	          Returns a translated string
upper()	              Converts a string into upper case
zfill()	              Fills the string with a specified number of 0 values at the beginning
'''
