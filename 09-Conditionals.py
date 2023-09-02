# ########################################################################################################################
# Conditionals
# ########################################################################################################################
# 
# In Python 3, "conditionals" refer to programming constructs that allow you to make decisions in your code based on certain conditions.
# They help your program execute different sets of instructions depending on whether a specified condition is true or false.
# 
# The primary conditional statements in Python are:
#
# If:  It is used to execute a block of code only if a specified condition is true.
# if condition:
#     Code to execute if condition is true
#
# else: It is used with if to execute a different block of code when the condition is false.
#
# if condition:
#      Code to execute if condition is true
# else:
#      Code to execute if condition is false
#
# elif (else if): It is used to check multiple conditions sequentially and execute the first block of code where the condition is true.
#
# if condition1:
#      Code to execute if condition1 is true
# elif condition2:
#     Code to execute if condition2 is true
# else:
#     Code to execute if neither condition1 nor condition2 is true
#
# Conditionals are fundamental for controlling the flow of your Python programs and making them responsive to different situations.
# They allow you to create dynamic and intelligent applications by directing the program's execution path based on the data and 
# conditions encountered during runtime.
# ########################################################################################################################

# This command will print true whenever the statement is true. In this case it would be true.
# Result: True

if True:
    print("True")

# This command will print false whenever the statement is false. Because this statement will never be false it will never print.
# Result: True

if False:
    print("False")

# This command will print "Not False" when the statement is not False.
# Results:
# True
# Not False

if not False:
    print("Not False")

# In the below statement if the statement is true then the following would be printed "1 < 1".
# Result: Because the state is not true it will not print.

if 1 < 1:
    print("1 < 1")

# In the below statement if 1 is less than or equal to 1 (1 <= 1) then print "1 <= "
# In this case it is True that 1 is equal to one so the following will happen.
# Result: 1 <= 1

elif 1 <= 1:
    print("1 <= 1")

#

