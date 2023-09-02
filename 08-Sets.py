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

