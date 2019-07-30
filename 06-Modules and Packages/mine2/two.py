#two.py

import one

print('Top level in two.py')

one.func()

if __name__ == "__name__":
	print("Two.py is being run directly")
else:
	print("Two.py has been imported")