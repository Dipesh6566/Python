# For Loop Variations

# 1.1 Using range() with Different Step Values
print("For loop with range and step:")
for i in range(0, 10, 2):  # Starts from 0, goes up to 10, with step 2
    print(i)  # Output: 0, 2, 4, 6, 8
    # Explanation: The `range()` function generates numbers from 0 to 9.
    # The third parameter (2) determines the step, meaning we skip every other number.
    # The loop prints numbers at intervals of 2 from 0 up to 8.

# 1.2 Iterating Over Multiple Sequences Using zip()
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print("\nFor loop with zip() over multiple lists:")
for num, letter in zip(list1, list2):  # Pairing up elements of both lists
    print(f"{num}: {letter}")  # Output: 1: a, 2: b, 3: c
    # Explanation: `zip()` combines two lists element by element.
    # For each iteration, it returns a pair of elements from `list1` and `list2`.
    # This makes it convenient to loop over multiple sequences in parallel.

# 1.3 Using List Comprehension
print("\nList Comprehension:", [x ** 2 for x in range(5)])  # Creates a list of squares: 0, 1, 4, 9, 16
    # Explanation: List comprehension allows for concise creation of lists.
    # The loop within the brackets iterates over the range from 0 to 4.
    # For each element, it squares the number (x**2) and stores it in a new list.

# 1.4 For Loop with else Clause
print("\nFor loop with else:")
for i in range(5):
    print(i)
else:
    print("Loop finished!")  # Output: Loop finished!
    # Explanation: The `else` clause runs after the `for` loop completes all iterations.
    # If the loop is terminated by `break`, the `else` block will not execute.
    # It's useful when you want to confirm that the loop ran to completion.

# 1.5 Using continue in a For Loop
print("\nFor loop with continue:")
for i in range(5):
    if i == 3:
        continue  # Skip printing 3
    print(i)  # Output: 0, 1, 2, 4
    # Explanation: `continue` skips the current iteration and moves to the next one.
    # When `i` is equal to 3, `continue` skips the `print(i)` statement.
    # This is helpful when you want to avoid certain values from being processed.

# 1.6 Using break in a For Loop
print("\nFor loop with break:")
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)  # Output: 0, 1, 2
    # Explanation: `break` immediately exits the loop when a condition is met.
    # In this case, the loop stops when `i` reaches 3, so it prints 0, 1, 2 only.
    # This is useful when you want to stop a loop early under specific conditions.


# While Loop Variations

# 2.1 While Loop with else Clause
counter = 0
print("\nWhile loop with else:")
while counter < 3:
    print(counter)
    counter += 1
else:
    print("While loop ended.")  # Output: While loop ended.
    # Explanation: The `while` loop runs as long as the condition is true.
    # The `else` clause executes when the condition becomes false (without a `break`).
    # It confirms that the loop has completed without interruptions.

# 2.2 Using continue in a While Loop
counter = 0
print("\nWhile loop with continue:")
while counter < 5:
    counter += 1
    if counter == 3:
        continue  # Skip the iteration when counter is 3
    print(counter)  # Output: 1, 2, 4, 5
    # Explanation: The `continue` skips the current iteration and moves to the next one.
    # If `counter` is 3, it skips the `print(counter)` statement.
    # This allows for conditional skipping within the loop.

# 2.3 Using break in a While Loop
counter = 0
print("\nWhile loop with break:")
while counter < 5:
    print(counter)
    counter += 1
    if counter == 3:
        break  # Exit the loop when counter reaches 3
    # Explanation: `break` stops the loop immediately when the condition is met.
    # Once `counter` equals 3, the loop terminates before printing 3, outputting 0, 1, and 2 only.
    # This is useful for stopping loops early under specific conditions.

# 2.4 Infinite While Loop (Use with caution)
print("\nInfinite While loop:")
while True:  # This loop will run forever until broken
    user_input = input("Type 'exit' to stop the loop: ")
    if user_input == 'exit':
        print("Loop ended.")
        break  # Exit the loop when 'exit' is typed
    # Explanation: `while True` creates an infinite loop.
    # The loop continues until a `break` statement is encountered.
    # It waits for user input and exits only when the user types 'exit'.

# While loop with For loop inside
print("\nWhile loop with for loop inside:")
counter = 0
while counter < 3:
    print(f"Outer loop iteration {counter}")
    for i in range(3):
        print(f"  Inner loop iteration {i}")
    counter += 1
    # Explanation: Nested loops are loops within loops.
    # Here, the `while` loop runs 3 times, and during each iteration, a `for` loop runs 3 times.
    # The result is a combination of both loops' outputs.

# Using break in Nested Loops
print("\nBreak in Nested Loops:")
for i in range(3):
    for j in range(3):
        if j == 2:
            break  # This only breaks the inner loop
        print(f"i={i}, j={j}")
    if i == 1:
        break  # Break the outer loop after the second iteration
    # Explanation: In nested loops, `break` can be used to break out of the inner loop.
    # The `break` statement inside the inner loop only stops that loop, not the outer one.
    # However, the second `break` stops the outer loop when `i` reaches 1.
