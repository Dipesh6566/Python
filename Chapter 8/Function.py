# In Python, we can define a function using the 'def' keyword followed by the function name and parentheses.
# The function may optionally accept arguments and return values, just like in other languages.

# Defining a simple function that prints a greeting message.
def greet():
    # This function doesn't take any arguments and simply prints a message
    print("Hello and good morning")

# Calling the greet function to display the message
greet()

# We can also pass arguments to a function to make it more flexible
def greet_with_name(name):
    # This function takes a 'name' argument and prints a personalized greeting message
    print("Hello " + name + ", good morning")

# Calling the function and passing "Dipesh" as an argument to personalize the greeting
greet_with_name("Dipesh")

# Python supports recursion, which means a function can call itself.
# This is useful for problems like calculating the factorial of a number.
def factorial(n):
    # Base case: if n is 0, return 1 (as the factorial of 0 is defined as 1)
    if n == 0:
        return 1
    else:
        # Recursive case: return n * factorial of (n-1)
        return n * factorial(n - 1)

# Calling the factorial function and passing 5 to calculate 5! (5 factorial)
print(factorial(5))  # Output: 120 (since 5! = 5 * 4 * 3 * 2 * 1 = 120)

# We can also store the return values of functions in variables.
# This allows us to perform operations with the returned value.
def greet_with_surname(surname):
    # This function takes a 'surname' argument, prints a greeting, and returns an integer value
    print("Hello " + surname + ", good morning")
    return 100  # Returning a value (an integer) from the function

# Storing the return value of the function in a variable
a = greet_with_surname("Mr.Patel")

# Printing the value stored in 'a', which was returned by the function greet_with_surname
# The value returned was 100, so this will output 100
print(a)  # Output: 100

# Functions in Python can return any type of data, including integers, floats, strings, or even other functions!
# The returned value is not limited to a specific data type.


# Defining a function with a default argument value
def greet_with_default(name="Guest"):
    """
    This function takes a 'name' argument. 
    If no 'name' is provided when calling the function, it defaults to "Guest".
    The function will print a greeting message using the provided or default name.
    """
    # Prints a personalized greeting message using the 'name' argument
    print(f"Hello, {name}, good morning!")
# this is a fstring its a way of printing.     


# Calling the function without providing an argument (defaults to "Guest")
greet_with_default()  # Output: Hello, Guest, good morning!
# In this case, no argument is passed, so the default value "Guest" is used.
# This is helpful when you want to provide a default greeting without always specifying a name.


# Calling the function with an argument
greet_with_default("Alice")  # Output: Hello, Alice, good morning!
# Here, "Alice" is passed as the argument, so the greeting is personalized to "Alice".



    
    