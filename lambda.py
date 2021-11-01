# lambda is a one line annonymous function

x = lambda x: x + 5
print(x(2))

# This is not the advised way to use a lambda

# map and filter make use of the lambda

x = [1,2,3,4,5,6,7,8,43345,7,234,5,3]
print(x)
# This will ad 2 to each and every value in the list that is defined in x
mp = map(lambda i: i + 2, x)
print(list(mp))

# Use lambda to only pull the even elements in the list then print
mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))