# #####################################################################################################################
# a tuple is an ordered collection of elements enclosed in parentheses ( ) and separated by commas. 
# Tuples are similar to lists, but they are immutable, which means their elements cannot be modified after creation.
# You can use tuples to store a fixed sequence of values, and they are often used for grouping related data together.
#
# my_tuple = (1, 2, 3, "Hello")
# In this example, my_tuple is a tuple containing four elements: two integers and two strings. 
# You can access tuple elements using indexing, just like you would with a list. For example:
#
# print(my_tuple[0])  # Output: 1
# print(my_tuple[3])  # Output: Hello
#
# Because tuples are immutable, you cannot change their elements or length once created. 
# This immutability makes them useful for situations where you want to ensure the data remains constant.
# #####################################################################################################################

# Tuple Items

tuple_items = ("item1", "item2", "item3")
print(tuple_items)
print(type(tuple_items))


# Tuple Numbers

tuple_numbers = (1, 2, 3)
print(tuple_numbers)
print(type(tuple_numbers))

# Tuple Repeat

tuple_repeat = ('Combine!',) * 4
print(tuple_repeat)
print(type(tuple_repeat))

# Mixed Tuple

mixed_tuple = ("A", 1, ("A", 1))
print(mixed_tuple)
print(type(mixed_tuple))

# Unable to Append a Tuple
# Example
# tuple_items.append("item4")

# Combinding Tuples

tuple_combined = tuple_items + tuple_numbers
print(tuple_combined)
print(type(tuple_combined))

# Unpacking Tuples

item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)

# Evaluate if the listed item is inside the tuple_items varable. Shows True or False Retults.

print("item1" in tuple_items)
print("item2" in tuple_items)
print("item3" in tuple_items)
print("item4" in tuple_items)

# Verifying Index of Tuples
# item 1 indexes to 0
# item 2 indexes to 1
# item 3 indexes to 2

print(tuple_items.index("item1"))
print(tuple_items.index("item2"))
print(tuple_items.index("item3"))

# Printing out the information indexed at 0,1,2

print(tuple_items[0])
print(tuple_items[1])
print(tuple_items[2])

# Tuple Length

print(len(tuple_items))

# Print Last Item in Tuple

print(tuple_items[-1])
print(tuple_items[-2])

# Slicing Tuple

print(tuple_items [0:2])
print(tuple_items [:2])
print(tuple_items [1:2])
print(tuple_items [-3:-1])

# Off Topic, but to show different examples of slicing.

string1 = "I am a string!"
print(string1[0:4])
print(string1[-1])
