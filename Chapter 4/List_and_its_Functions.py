# In Python, we have lists where we can store data in a sequential manner.
# They are like arrays from other languages, but in lists, we can store int, float, string—all data types in a single list.
# We can also store lists inside a list.
list0 = [12, 34, 56, 78, 90, 122, 467, 543]
print(list0)

list1 = ["Apple", 10, 109, 54.16, 89, 2.6, "Orange"]
print(list1)  # Output: ['Apple', 10, 109, 54.16, 89, 2.6, 'Orange']
#strings in list are mutable that means
# we can change them unlike normal strings which are immutable
list1[0] = "Banana"
print(list1)  # Output: ['Banana', 10, 109, 54.16, 89, 2.6, "Orange"]


# We can also store lists inside a list
list2 = [["Apple", 10], [109, 54.16], [89, 2.9, "Orange"]]
print(list2)  # Output: [['Apple', 10], [109, 54.16], [89, 2.9, 'Orange']]

# There are many functions (methods) to do operations on the list,
# like sort(), reverse(), append(), insert(), pop(), remove(), etc.

# Sorting list0 in ascending order
list0.sort()
print(list0)  # Output: [12, 34, 56, 78, 90, 122, 467, 543]

# Reversing the elements of list1
list1.reverse()
print(list1)  # Output: ['Orange', 2.6, 89, 54.16, 109, 10, 'Apple']

# Adding (appending) "Dipesh" to the end of list1
list1.append("Dipesh")
print(list1)  # Output: ['Orange', 2.6, 89, 54.16, 109, 10, 'Apple', 'Dipesh']

# Inserting "Patel" at index 3 in list1
list1.insert(3, "Patel")
print(list1)  # Output: ['Orange', 2.6, 89, 'Patel', 54.16, 109, 10, 'Apple', 'Dipesh']

# Removing the item at index 3 from list1
popped_item = list1.pop(3)
print(popped_item)  # Output: 'Patel'
print(list1)  # Output: ['Orange', 2.6, 89, 54.16, 109, 10, 'Apple', 'Dipesh']

# Removing "Dipesh" from list1
list1.remove("Dipesh")
print(list1)  # Output: ['Orange', 2.6, 89, 54.16, 109, 10, 'Apple']

# Using index() function to get the index of 54.16 in list1
index = list1.index(54.16)
print(index)  # Output: 3

# Using count() function to get the count of repetitions of "Apple" in list1
count_apple = list1.count("Apple")
print(count_apple)  # Output: 1

# Using len() function to get the length of list1
print(len(list1))  # Output: 7

# Using any() to check if "Dipesh" exists in list1
# any() returns True if at least one element in the iterable evaluates to True.
# Here, we check each item in list1 to see if it equals "Dipesh".
print(any(item == "Dipesh" for item in list1)) 
# Output: False (because "Dipesh" is not in list1)

# Using all() to check if all elements in list1 are truthy
# all() returns True only if all elements in the iterable evaluate to True.
# bool(item) converts each item into a boolean 
# (e.g., non-zero numbers and non-empty strings are True, while 0, None, and empty strings are False).
print(all(bool(item) for item in list1)) 
# Output: True (because all elements in list1 are truthy)

# Copying list1 into a new list
list_copy = list1.copy()
print(list_copy)  # Output: ['Orange', 2.6, 89, 54.16, 109, 10, 'Apple']

# Extending list1 with another list
list1.extend([300, 400, 500])
print(list1)  # Output: ['Orange', 2.6, 89, 54.16, 109, 10, 'Apple', 300, 400, 500]

# Clearing all elements from list1
list1.clear()
print(list1)  # Output: []

# Using slicing to access parts of a list
list0 = [12, 34, 56, 78, 90, 122, 467, 543]
print(list0[2:5])  # Output: [56, 78, 90] (slicing from index 2 to 4)

# Checking if an element exists in the list
print(90 in list0)  # Output: True

# Concatenating two lists
new_list = list0 + [1000, 2000, 3000]
print(new_list)  # Output: [12, 34, 56, 78, 90, 122, 467, 543, 1000, 2000, 3000]

# Repeating a list
repeated_list = list0 * 2
print(repeated_list)  # Output: [12, 34, 56, 78, 90, 122, 467, 543, 12, 34, 56, 78, 90, 122, 467, 543]


