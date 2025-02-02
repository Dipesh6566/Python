# Sets in Python are unordered collections of unique elements.
# They do not allow duplicate element and are highly efficient for membership tests (checking if an item exists).

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating an empty set
# Use set() to create an empty set, as {} creates an empty dictionary.
empty_set = set()
print(empty_set)  # Output: set()

# Adding elements to a set
# Use add() to insert a single element into the set.
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Adding multiple elements using update()
# update() allows you to add multiple items (can be a list, tuple, or another set).
my_set.update([7, 8, 9])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Removing elements using remove()
# remove() deletes a specific element. It raises an error if the element is not found.
my_set.remove(9)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Removing elements using discard()
# discard() also deletes a specific element but does not raise an error if the element is not found.
my_set.discard(8)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}
my_set.discard(100)  # No error even though 100 is not in the set.

# Removing a random element using pop()
# pop() removes and returns an arbitrary element from the set.
random_element = my_set.pop()
print(random_element)  # Output: (varies)
print(my_set)  # Output: Remaining elements, order is arbitrary.

# Clearing all elements from the set
# clear() removes all elements from the set, leaving it empty.
my_set.clear()
print(my_set)  # Output: set()

# Set operations (union, intersection, difference, symmetric difference)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union using union() method
# Combines all unique elements from both sets.
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection using intersection() method
# Retrieves only the elements common to both sets.
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3, 4}

# Difference using difference() method
# Retrieves elements that are in the first set but not in the second.
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}

# Symmetric Difference using symmetric_difference() method
# Retrieves elements that are in either set, but not in both.
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 5, 6}

# Checking subset and superset relationships
# issubset() checks if all elements of a set are contained in another set.
print({1, 2}.issubset(set_a))  # Output: True

# issuperset() checks if a set contains all elements of another set.
print(set_a.issuperset({1, 2}))  # Output: True

# Checking disjoint sets
# isdisjoint() checks if two sets have no elements in common.
print(set_a.isdisjoint({5, 6}))  # Output: True

# Copying a set
# Use copy() to create a shallow copy of a set.
set_copy = set_a.copy()
print(set_copy)  # Output: {1, 2, 3, 4}

# Length of a set
# Use len() to get the number of elements in a set.
print(len(set_a))  # Output: 4

# Checking membership
# Use the "in" keyword to check if an element is in the set.
print(3 in set_a)  # Output: True
print(10 in set_a)  # Output: False
