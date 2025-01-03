
a = input("Enter the value for a:")
'''is we print this a we will get string because normal input takes string as input no matter the value we enter even if its int of float'''
print(a) # this will print the value of a as string even if we see number but its a string you can check by adding it in some other variable 
#if we want proper int or float inputs then we need to typecast  the inputs
# typecasting is the process of converting one data type to another data type
# we can use int() or float() to typecast the inputs
# lets see how to do it
b = int(input("Enter the value for b:"))
print(b) 