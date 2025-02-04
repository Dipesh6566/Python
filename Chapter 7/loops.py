# Loops are used in Python to repeatedly execute a block of code.
# We can use different types of loops like `for` loops and `while` loops.
# The `for` loop is generally used when we know the number of iterations, or when we iterate over sequences (like lists, tuples, strings).
# The `while` loop is used when we don't know how many times we need to iterate and continue looping as long as a condition is True.

# Example 1: Simple for loop to iterate over a range
# A `for` loop is typically used to iterate over a sequence of elements.
# Here, we use `range()` to repeat the loop 5 times, from 0 to 4 (range is exclusive of the upper limit).
print("Simple For Loop:")
for i in range(5):  # Iterates 5 times, i takes values from 0 to 4
    print(f"Iteration {i + 1}")  # Output: Iteration 1, Iteration 2, ..., Iteration 5

# Example 2: For loop to iterate over a list
# This is used when you want to loop through elements of a list.
fruits = ["Apple", "Banana", "Orange"]
print("\nFor Loop with List:")
for fruit in fruits:  # Iterates through each element in the list `fruits`
    print(fruit)  # Output: Apple, Banana, Orange

# Example 3: For loop with the `enumerate()` function
# `enumerate()` gives us both the index and value of each element while iterating.
print("\nFor Loop with enumerate():")
for index, fruit in enumerate(fruits):  # index gives position and fruit gives the value
    print(f"Index {index}: {fruit}")  # Output: Index 0: Apple, Index 1: Banana, Index 2: Orange

# Example 4: For loop with a condition
# We can add a condition inside a `for` loop to check values or perform specific actions.
print("\nFor Loop with Condition:")
for i in range(10):  # Loop from 0 to 9
    if i % 2 == 0:  # Check if the number is even
        print(f"{i} is even.")  # Output: 0 is even, 2 is even, 4 is even, ...

# Example 5: Nested for loops
# We can have loops inside other loops, called nested loops, useful for multi-dimensional data.
print("\nNested For Loops:")
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i = {i}, j = {j}")  # Output: i=0, j=0, i=0, j=1, i=1, j=0, ...

# Example 6: While loop
# A `while` loop keeps executing as long as the condition is true.
# Be careful, as it could lead to an infinite loop if the condition never becomes False.
print("\nWhile Loop:")
counter = 0
while counter < 5:  # Loop runs while counter is less than 5
    print(f"Counter: {counter}")  # Output: Counter: 0, Counter: 1, ..., Counter: 4
    counter += 1  # Increment counter by 1 after each loop

# Example 7: Infinite while loop (be careful with this)
# A `while` loop can run indefinitely if the condition is always true.
# You can use `break` to stop the loop when needed.
print("\nInfinite While Loop with break:")
while True:  # This creates an infinite loop
    user_input = input("Enter 'stop' to break the loop: ")  # Prompt user for input
    if user_input == "stop":  # If user types 'stop', exit the loop
        print("Loop stopped.")
        break  # Exit the loop
    print(f"You entered: {user_input}")
