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

# Should either of the above commands not be true then the following else statement would print "No Statement is True"
# In this example the else statement would never be called unless varables are changed in the previous lines.

else:
    print("No Statement is True")

# Expanding on the above example we add in a 2nd elif and intentionally make sure the first elif is not true forcing it to go to the
# next line. Because 2 is >= to 2 the following will print "2 >= 2"
# Result: 2 >= 2

if 1 < 1:
    print("1 < 1")
elif 1 > 1:
    print("1 > 1")
elif 2 >= 2:
    print("2 >= 2")
else:
    print("No Statement is True")

# In this example we are using 2 statements connected by the "and" command. In order for this statement to be True both
# statements must be true otherwise it will be False
# Results: 1 > 0 and 0 < 1

if 1 > 0 and 0 < 1:
    print("1 > 0 and 0 < 1")

# In this example only 1 of the statements is true so it is considered False triggering the "No Statement is True" message.
# Result: No Statement is True

if 1 > 0 and 0 > 1:
    print("1 > 0 and 0 > 1")
else:
    print("No Statement is True")

# Using the or option in place of the and option allows 1 of the 2 statements to be true preventing the else statement from being used.
# Results: 1 > 0 or 0 < 1

if 1 > 0 or 0 > 1:
    print("1 > 0 or 0 < 1")
else:
    print("No Statement is True")

# In the below example only 1 of the 2 statements to the left of the and have to be true in addition to the 1 statement on the right
# also has to be true for the "1 > 0 or 0 < 1 and 1 == 1" statement to print.
# Results: 1 > 0 or 0 < 1 and 1 == 1

if (1 > 0 or 0 > 1) and 1 == 1:
    print("1 > 0 or 0 < 1 and 1 == 1")
else:
    print("No Statement is True")

# Shorter version of a previous command.
# Results: 0 < 1

if 0 < 1: print("0 < 1")

# Another shortened version example.
# Result: 1 >= 1

print("1 >= 1") if 1 >= 1 else print ("1 < 1")






