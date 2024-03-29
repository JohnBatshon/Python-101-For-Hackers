# ####################################################################################################################################
# Dictionaries
# ####################################################################################################################################
# A data structure that stores key-value pairs.
# Unordered and mutable, meaning you can change its content.
# Created using curly braces {} or the dict() constructor.
# Accessed and manipulated using keys.
# Keys are unique and must be immutable (e.g., strings, numbers).
# Values can be of any data type (e.g., numbers, strings, lists).
#
# Example
#
# my_dict = {"name": "John", "age": 30}
# print(my_dict["name"])  # Output: "John"
#
# Dictionaries are commonly used for mapping relationships between data.
# ####################################################################################################################################

dict1 = {"a":1, "b":2, "c":3}
print(dict1)
print(type(dict1))
print(len(dict1))

# Printing out the key value linked to "a" which results in 1
# Index cannot be used with dictionaries i.e. [0] will not work.

print(dict1["a"])
print(dict1.get("a"))

# This command will print all keys available within the dict1 dictionary.
# The response should show dict_keys(['a', 'b', 'c'])

print(dict1.keys())

# To print out all values within a dictionary the .values command can accomplish this.
# Results: dict_values([1, 2, 3])

print(dict1.values())

# Using the .items command will print out all items within the dictionary
# Results: dict_items([('a', 1), ('b', 2), ('c', 3)])

print(dict1.items())

# The below command will not work because "a" has already been assigned.
# Results (No Change): {'a': 1, 'b': 2, 'c': 3}

print(dict1)
dict1["a"] = 1
print(dict1)

# Since "d" was not assigned I was able to add in a value for "d" of 4
# Results: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(dict1)
dict1["d"] = 4
print(dict1)

# Changing the Value of Key "A". Changed from 1 to 0
# Results: {'a': 0, 'b': 2, 'c': 3, 'd': 4}
print(dict1)
dict1["a"] = 0
print(dict1)

# Using the .update command we can change the key value of "a" back to 1
# Results: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(dict1)
dict1.update({"a": 1})
print(dict1)

# Using the .pop command to remove a key value
# Results: {'a': 1, 'b': 2, 'c': 3}

print(dict1)
dict1.pop("d")
print(dict1)

# Using the del command to remove a key value
# Results: {'a': 1, 'b': 2}

print(dict1)
del dict1["c"]
print(dict1)

# Adding a value in for key "c"
# Results:
# {'a': 1, 'b': 2}
# {'a': 1, 'b': 2, 'c': {'a': 1, 'b': 2}}

print(dict1)
dict1["c"] = {"a":1, "b":2}
print(dict1)

# Empty Dictionary Example 1
# Results: []

dict2 = []
print(dict2)

# Empty Dictionary Example 2
# Results: ()

dict3 = ()
print(dict3)
