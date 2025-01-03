
a = 10
'''in python we can just initialize the variable without assigning it any data types cause python will do it self
. The type() function gives us type of data of the passed variable '''

print(type(a))  # Output: <class 'int'>
e = True
b = False 
''' this are the boolean types of variables we can also use different types of operators
like ==, !=, >, <, >=, <=, and, or, not . Here and,or,not are the logical operators which give  us value according to the truth table of the their logic gates '''

print(type(e))  # Output: <class 'bool'>

# for Logical gates 
# dont live space in python cause it is important for syntax of py 
c = True or False #it is an OR gate operator so atleast one value needs to be true for the variable value to be true 
d = True and False # it is an AND gate operator so both needs to be TRUE for the value of the operator be true 
print(c)  # Output: True
print(d)  # Output : False
''' Typecasting is also in python'''
f = 50.60
#its a float but will give int as answer cause its typecasted 
g = int(f)
print(g)  # Output: 50
''' we can also typecast int to float'''
h = float(g)
print(h)  # Output: 50.0
''' we can also typecast int to str '''
i = str(g)
print(i)  # Output: '50'
''' we can also typecast str to int '''
j = int(i)
print(j)  # Output: 50
''' we can also typecast str to float '''
k = float(i)
print(k)  # Output: 50.0
''' we can also typecast float to str '''
l = str(k)
print(l)  # Output: '50.0'

a1 = 10
print(a1)
# Output: 10
a1+=3 # this += operator is used to increment and decrement any variable by the num,ber we want.
#  where we have written 3, we acn write any number at that place 
print(a1) 


