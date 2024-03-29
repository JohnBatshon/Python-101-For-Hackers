# ##############################################################################################################################
# Lists
# ##############################################################################################################################
#
# A data structure that stores a collection of items.
# Ordered and mutable, meaning you can change its elements.
# Created using square brackets, like my_list = [1, 2, 3].
# Supports various operations like appending, slicing, and sorting.
# Allows mixed data types within the same list.
# Accessed by index, starting at 0.
# 
# Example Code
#
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # Output: [1, 2, 3, 4]
#
# Lists are a fundamental part of Python's data structures.
#
# ##############################################################################################################################

# Simple List showing basic data

list1 = ["A", "B", "C", "D", "E", "F"]
print(list1)

# List example showing many types of data from Strings, Integers, Floats, Boolean

list2 = ["A", 1, 2.0, ["A"], [], list(), ("A"), False]
print(list2)
print(type(list2))

# Printing out single items from the list
# Example Printing First Item in a List [0]
# Example Printing Last Item in a list [-1]

print(list1[0])
print(list1[-1])

# In the example below the printed results will be the same for the following reasons
# When printing the item indexed at spot 3 the starting point is set at 0 wich is the first index point.
# Setting that index point at -1 also will generate the same results.

print(list2[3][0])
print(list2[3][-1])

# Example of changing the first item in the list from its original value A to its new value of X

list1[0] = "X"
print(list1)

# Example showing deleting the first index of list 1

print(list1)
del list1[0]
print(list1)

# Adding back in the previous value of A into List1 Index 0

list1.insert(0, "A")
print(list1)

# Removing the newly added "A" from Index 0
# Make sure to check your work and select the correct index
# I had mistakenly used index 1 thinking it was index 0
# I had to go back and fix this after reviewing unexpected results

del list1[0]
print(list1)

# Adding the recently removed "A" from Index 0

list1 = ["A"] + list1
print(list1)

# Using the .append command we can add in another item to our list at the end.
# In this example I have appended "G" to list1

list1.append("G")
print(list1)

# Printing Lists "Max" and "Min" (i.e. the beginding and end of a list)
# Printing max will print the last index in the list
# Printing min will print the first index in the list

print(max(list1))
print(min(list1))

# How to Identify the index number of data in a field using the .index command

print(list1.index("C"))
print(list1[list1.index("C")])

# Printing a list in reverse with .reverse

print(list1)
list1.reverse()
print(list1)

# Reversing a list can be done with this method causing the list to be printed from the end towards the begining.
# [::-1] is a slicing operation that specifies a start, stop, and step value for indexing the list.
# So, when you execute list1 = list1[::-1], it creates a reversed copy of list1 and assigns it back to list1.
# As a result, list1 will now contain its elements in reverse order.
# For example, if list1 was initially [1, 2, 3, 4], after this operation, it will become [4, 3, 2, 1].

list1 = list1[::-1]
print(list1)

# Using the .count command will count how many matching objects are indexed in the list
# Additionally I have appended an additional A and then reran the command and the result changed from 1 to 2

print(list1.count("A"))
list1.append("A")
print(list1)
print(list1.count("A"))

# The .pop command can remove an indexed item from a list.
# In this example the last entry is being removed.

print(list1)
list1.pop()
print(list1)

# Creating List 3

list3 = ["H", "I", "J"]
print(list3)

# Using the .extend command we can add list 3 to the end of list 1

print(list1)
list1.extend(list3)
print(list1)

# Using the .clear command will remove all data from a list

list1.clear()
print(list1)

# Sorting Lists
# Using the .sort command will sort the list out in the example below

list4 = [8, 12, 5, 6, 17, 2]
print(list4)
list4.sort()
print(list4)

# Reverse sorting a list
# Note: Types are a sure way to make your commands fail
# Learnt to type & spell >_>

print(list4)
list4.sort(reverse=True)
print(list4)

# When copying a list from a list the data in both lists will change causing unintended issues
# In the example below we changed a value in list5 and then printed list 4 & 5 and they bow show the change.

list5 = list4
print(list5)
print(list4)

list5[2] = "X"
print(list5)
print(list4)

# To overcome the problem above using the .copy command will assist with this problem.
# In the below example we sucessfully changed the data in list 6 without modifying the data in list 4

list6 = list4.copy()
print(list4)
print(list6)

list6[2] = "A"
print(list4)
print(list6)

# Creating a new list (list7)

list7 = ["1", "2", "3"]
print(list7)

# Using the map command
# map(float, list7) applies the float function to each element in list7.
# This means it attempts to convert each element in list7 to a floating-point number (decimal number).
# For example, if list7 is [1, 2, 3], map(float, list7) would result in the iterable [1.0, 2.0, 3.0].
# list(...) converts the result of the map operation into a new list.
# So, list8 will be a new list containing the elements from list7, but with each element converted to a floating-point number.
#
# list7 = ["1.1", "2.2", "3.3"]
# list8 = list(map(float, list7))
# print(list8)  # Output: [1.1, 2.2, 3.3]
#
# In this example, list8 will contain floating-point numbers derived from the string representations in list7.

list8 = list(map(float, list7))
print(list8)







