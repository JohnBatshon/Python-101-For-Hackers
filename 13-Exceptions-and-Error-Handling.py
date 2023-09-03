# ##############################################################################################################################
#
# Exceptions and Error Handling
#
# ##############################################################################################################################
#
# In Python 3, exceptions are unexpected events or errors that can occur during program execution. Error handling is the process of dealing with these exceptions to prevent a program from crashing. Here's a very short summary:
#
# Exception: An exception is a runtime error that can occur during program execution, such as division by zero or trying to access a non-existent file.
# Try-Except Block: To handle exceptions, you can use a try block to enclose the code that might raise an exception. If an exception occurs, the program jumps to the corresponding except block.
# Except Block: The except block specifies how to handle the exception. You can catch specific exceptions or use a general except block to catch all exceptions.
# Finally Block (Optional): You can use a finally block to specify code that always runs, whether an exception occurs or not. This block is optional.
# Example:
#
# try:
#    result = 10 / 0  # This will raise a ZeroDivisionError
# except ZeroDivisionError:
#     print("Error: Division by zero")
# except Exception as e:  # Catch all other exceptions
#     print("An error occurred:", str(e))
# finally:
#     print("This will always execute")
# In this example, a try block attempts a division by zero, which raises a ZeroDivisionError. The program then handles the exception by printing an error message. Finally, the finally block executes regardless of whether an exception occurred or not.
#
# #############################################################################################################################

print(1)
print(2)

#try:
#    abdfsdjfslkfsd

#except:
#    print("The file does not exist!")

try:
#    RandomGarbageText
    f = open("Made_up_file_name.txt")
except FileNotFoundError:
    print("The file does not exist!")
except Exception as e:
    print(e)
finally:
    print("this message!")

n = 100
if n == 0:
    raise Exception("n can't be 0!")
if type(n) is not int:
    raise Exception("n must be an int!")
print(1/n)

n = 1
assert(n != 0)
print(1/n)

