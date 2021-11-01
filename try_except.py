# Handling Exceptions

# This bit of code will cause a traceback, you cant divide by 0. Your program gets killed.
# x = 7 / 0

# Use the try except block
# This will raise the error but not show it as a traceback. The program still runs. 
try:
    x = 7 / 0
except Exception as e:
    print(e)

# finally block. Usually this is where you place clean up type operations
finally:
        print('finally')