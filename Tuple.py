# Tuples are immutable collections that store elements in a fixed order.
# You cannot change, add, or remove elements after a tuple is created.
# Tuples can store any data type, and they are similar to lists but immutable.

# Defining tuples
tuple1 = (10, 20, 30, 40, 50)
tuple2 = ("Apple", "Banana", "Cherry", "Apple")
tuple3 = (1, 2, 3, (4, 5), "Hello", 6.7)

# Printing the tuples
print(tuple1)  # Output: (10, 20, 30, 40, 50)
print(tuple2)  # Output: ('Apple', 'Banana', 'Cherry', 'Apple')
print(tuple3)  # Output: (1, 2, 3, (4, 5), 'Hello', 6.7)

# Accessing elements using indexing
# Indexing starts from 0 for the first element.
print(tuple1[2])  # Output: 30 (third element in the tuple)

# Accessing elements using negative indexing
# Negative indexing starts from -1 for the last element.
print(tuple2[-1])  # Output: 'Apple' (last element in the tuple)

# Slicing a tuple
# Slicing allows you to extract a portion of the tuple using start and end indices.
# It includes elements from the start index to one before the end index.
print(tuple1[1:4])  # Output: (20, 30, 40)

# Checking the length of a tuple
# len() returns the total number of elements in the tuple.
print(len(tuple3))  # Output: 6

# Checking if an element exists in a tuple
# Use the "in" keyword to check if a value is present in the tuple.
# It returns True if the element is found, otherwise False.
print("Banana" in tuple2)  # Output: True

# Counting occurrences of an element in a tuple
# count() tells you how many times a specific value appears in the tuple.
print(tuple2.count("Apple"))  # Output: 2

# Finding the index of the first occurrence of an element
# index() returns the position of the first appearance of the value.
print(tuple2.index("Cherry"))  # Output: 2

# Concatenating two tuples
# The + operator combines two tuples into one.
# The result is a new tuple; the original tuples are not modified.
tuple4 = tuple1 + tuple2
print(tuple4)  # Output: (10, 20, 30, 40, 50, 'Apple', 'Banana', 'Cherry', 'Apple')

# Repeating a tuple
# The * operator creates a new tuple by repeating the original tuple multiple times.
tuple5 = tuple1 * 2
print(tuple5)  # Output: (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

# Iterating through a tuple
# Use a for loop to access each element of the tuple one by one.
# Here, we print all elements in tuple1 on the same line.
for item in tuple1:
    print(item, end=" ")  # Output: 10 20 30 40 50

# Using min() and max() with numeric tuples
# min() gives the smallest value in the tuple, and max() gives the largest.
print(min(tuple1))  # Output: 10
print(max(tuple1))  # Output: 50

# Using sum() with numeric tuples
# sum() adds up all the numeric elements in the tuple.
print(sum(tuple1))  # Output: 150

# Accessing elements in nested tuples
# Nested tuples are tuples inside another tuple.
# You can access nested elements using multiple levels of indexing.
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple[1])      # Output: (2, 3)
print(nested_tuple[1][1])   # Output: 3

# Unpacking tuples
# Unpacking allows you to assign each element of a tuple to a variable.
# The number of variables must match the number of elements in the tuple.
a, b, c = (100, 200, 300)
print(a, b, c)  # Output: 100 200 300

# Using tuple() to convert other iterables into tuples
# The tuple() function takes a list or other iterable and converts it to a tuple.
list_to_tuple = tuple([1, 2, 3, 4])
print(list_to_tuple)  # Output: (1, 2, 3, 4)
