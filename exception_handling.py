# Some errors are not fixable like SyntaxError, IndentationError, TabError, SystemExit, KeyboardInterrupt, MemoryError, RecursionError.

# a=12
# if a>10:
# print("a is greater than 10") #this gives IndentationError because the print statement is not indented properly.

# Some errors are fixable like NameError, TypeError, ValueError, ZeroDivisionError, IndexError, KeyError, AttributeError, ImportError, ModuleNotFoundError.
# And these are the errors that we can handle using try and except blocks.

try:
    reult = 10/0
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("Division successful.")

finally:
    print("This block will always execute.")