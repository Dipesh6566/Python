# If-Else and Elif in Python are used to make decisions based on conditions.

# Example 1: Using if-else
# The `if` statement checks a condition and runs a block of code if the condition is true.
# If the condition is false, the `else` block runs instead.

x = 10
if x > 5:  # Check if x is greater than 5
    print("x is greater than 5")  # Output: x is greater than 5
else:  # This block will run if the condition in `if` is false.
    print("x is not greater than 5")

# Example 2: Using elif (else if)
# The `elif` statement allows us to check multiple conditions.
# It checks a new condition if the previous condition in `if` (or `elif`) is false.

y = 20
if y < 10:  # Check if y is less than 10
    print("y is less than 10")
elif y == 20:  # Check if y is exactly 20
    print("y is 20")  # Output: y is 20
else:  # This block runs if both `if` and `elif` are false
    print("y is greater than 10 but not 20")

# Example 3: Multiple elif statements
# You can have multiple `elif` statements to check different conditions one after another.

age = 25
if age < 18:  # Check if age is less than 18
    print("You are a minor.")
elif 18 <= age < 30:  # Check if age is between 18 and 29
    print("You are a young adult.")  # Output: You are a young adult.
elif 30 <= age < 60:  # Check if age is between 30 and 59
    print("You are an adult.")
else:  # This block runs if none of the above conditions are true (i.e., age is 60 or older)
    print("You are a senior citizen.")

# Example 4: Using if-else with boolean conditions
# `if-else` is frequently used for handling boolean expressions (True/False).

is_sunny = True
if is_sunny:  # If the weather is sunny (True), do something
    print("Let's go outside!")  # Output: Let's go outside!
else:  # If it's not sunny (False), do something else
    print("Let's stay indoors.")
