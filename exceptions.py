"""
Errors detected during execution are called exceptions and are not unconditionally fatal
You can raise an exception with raise
"""
raise Exception('Bad')
# Other possible uses of raise include the FileExistsError
raise FileExistsError('The file already exists')

# See try_except.py on how to handle an errors
