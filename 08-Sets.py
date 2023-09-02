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

# Using updating a set with the .update command from a stored list.
# Results:
# ['a', 'b', 'c']
# {4, 5, 6}
# {4, 5, 6, 'b', 'c', 'a'}

list1 = ["a", "b", "c"]
set4 = {4, 5, 6}
print(list1)
print(set4)

set4.update(list1)
print(set4)

# Using the .union command we can create a new set using set4.union(set5)
# The results of set 6 should be the data from set4 + set5
# Results:
# {'a', 4, 5, 6, 'b', 'c'}
# {8, 9, 7}
# {'a', 4, 5, 6, 'b', 8, 9, 7, 'c'}

set5 = {7, 8, 9}
set6 = set4.union(set5)
print(set4)
print(set5)
print(set6)

# Using the .remove command from a set
# Results:
# {4, 5, 6, 'a', 'c', 'b'}
# {5, 6, 'a', 'c', 'b'}

print(set4)
set4.remove(4)
print(set4)

# Using .discard will remove the specified value without throwing out an error if the value doesn't exist
# Results
# {5, 6, 'a', 'b', 'c'}
# {5, 6, 'a', 'c'}

print(set4)
set4.discard("b")
print(set4)

# Although .pop can be used to remove data since a set's data can be random you will not have control over what is actually removed.
# Results:
# {'a', 'd', 'c', 'b'}
# {'d', 'c', 'b'}

print(set1)
set1.pop()
print(set1)

