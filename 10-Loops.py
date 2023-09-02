# ##################################################################################################################################
# Loops
# ##################################################################################################################################
#
# In Python 3, "loops" are programming constructs that allow you to repeat a set of instructions multiple times,
# making your code more efficient and less repetitive.
# They are like a recipe that you follow repeatedly until a certain condition is met.
#
# There are two primary types of loops in Python:
#
# for loop: A for loop is used when you know in advance how many times you want to repeat a block of code.
# It iterates over a sequence (like a list or range) and performs the specified actions for each item in the sequence.
#
# for item in sequence:
#     Code to execute for each item in the sequence
#
# while loop: A while loop is used when you want to repeat a block of code as long as a certain condition is true.
# It keeps looping until the condition becomes false.
#
# while condition:
#     Code to execute while the condition is true
#
# Loops are incredibly useful for tasks such as processing data, performing repetitive calculations,
# or iterating through collections of items.
# They help you automate tasks and make your code more flexible and powerful.
#
# ##################################################################################################################################

# Although you can use a command like the below example it is not best practice and leaves room for human error.
# Result:
# 1
# 2
# 3

a = 1
print(a)
a += 1
print(a)
a += 1
print(a)

print("---")

# Using a while loop in the example below will keep running until a no longer less than 5
# Results:
# 1
# 2
# 3
# 4
# 5

a = 1
while a < 5:
    a += 1
    print(a)

print("---")

# In the for loop we specify multiple times triggering it to run the command i+6 against each variable.
# Results:
# 6
# 7
# 8
# 9
# 10

for i in [0, 1, 2, 3, 4]:
    print(i+6)

print("---")

# Using the range command we are limiting to no more than 5 entires.
# Resulting: 6 7 8 9 10

for i in range(5):
    print(i+6)

print("---")

#

for i in range(3):
    for j in range (3):
        print(i,j)

print("---")

# In this example i will increase by 1 until it hits 2 then the loop will break.
# Result 0 1

for i in range(5):
    if i == 2:
        break
    print(i)

print("---")

# In this example using the continue parameter will continue the process without hitting the print(i) command when i = 2
# Resulting: 0 1 3 4

for i in range(5):
    if i == 2:
        continue
    print(i)

print("---")

# When using the pass control statement when i == 2 it will trigger the pass command and move onto the next action print(i)
# Resulting: 0 1 2 3 4

for i in range(5):
    if i == 2:
        pass
    print(i)

print("---")

# So in this example we use a string in place of a number. The command will cycle through the word "string" and each time it will
# pass 1 letter through and then print it in the 2nd lind of code.
# Resulting: s t r i n g

for c in "string":
    print(c)

print("---")

# In this example we use a key + value set and run the command over each of the 3 indexed items.
# Results:
# a 1
# b 2
# c 3

for key, value in {"a":1, "b":2, "c":3}.items():
    print(key, value)

print("---")
