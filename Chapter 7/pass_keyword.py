# Example 1: Using pass in an if-else statement
x = 5
if x > 10:
    pass  # This block does nothing if x is greater than 10, can be implemented later
else:
    print("x is 5 or less")  # Executes because x is not greater than 10

# Example 2: Using pass in a loop
for i in range(3):
    if i == 1:
        pass  # Do nothing if i is 1, placeholder for future logic
    else:
        print(i)  # Print i when it is not 1
        
# we can also use them for code which are not done yet 
# but we need to check the rest of the code if it is running or not
# so we write pass keyword below the code which is not complete yet code
# because of pass keyword the interpreter will not give any error
for i in range(10):
    pass
# now this code is not finished yet 
# so if we write pass keyword in itt it will give us 
# no error and we can finish it later after checking the rest of the code

