# ##############################################################################################################################
# Sets
# ##############################################################################################################################
# A data structure that stores a collection of unique elements.
# Unordered and mutable (for adding/removing elements), but the elements themselves are immutable.
# Created using curly braces {} or the set() constructor.
#
# Example
#
# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)  # Output: {1, 2, 3, 4}
#
# Sets are useful for tasks that require unique values or testing membership in a collection.
# ##############################################################################################################################

# Example Set
# Results:
# {'a', 'c', 'b'}
# <class 'set'>
#
# Note: With sets you cannot specify an order and if you rerun the program the order will likely display in a different order.
# {'c', 'b', 'a'}
# {'b', 'a', 'c'}
# And so on...

set1 = {"a", "b", "c"}
print(set1)
print(type(set1))

# Sets cannot be printed by index because they are not indexed. The below command will trigger an error.
# print(set1[0])
# TypeError: 'set' object is not subscriptable

# Sets will not retain duplicate values.
# Example: set2 = {"a", "a", "a"}
# Results: {'a'}

set2 = {"a", "a", "a"}
print(set2)
print(len(set2))

# Sets can hold different data types i.e. Strings, Integers, Booleans
# Results: {0, True, 'a'}

set3 = {"a", 0, True}
print(set3)

# Another example
# Results: {'b', 1, False}

set4 = set(("b", 1, False))
print(set4)

# Adding a value to a set with the .add command
# Results:
# {'c', 'a', 'b'}
# {'c', 'd', 'a', 'b'}

print(set1)
set1.add("d")
print(set1)

# Updating Sets with the .update command
# In the below command we are updating set3 with set4 to pull in the values of set4 into set3
# Sets cannot have duplicates so only unique data is added.
# Results:
# {0, True, 'a'}
# {False, 1, 'b'}
# {0, True, 'b', 'a'}

print(set3)
print(set4)
set3.update(set4)
print(set3)

#





