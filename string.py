a ='Dipesh'

b = "Dipesh"
# this two above are the methods to print string in Pythone
c = '''ThisIsTheFileCreatedByDipesh''' # This is to store multiline string
print(c) # This is to print the string

'''There is a lenth function for string
which returns the length of the string'''
print(len(c)) # This is to print the length of the string
#there is a slice function for python too
#slice function is used to get the part of the string
print(a[0:5]) # This is to print the first five character of the string
# in this a[m:n] it will print from 0 to 4th that means m to (n-1)th character of this string
# This is to print the first ten character of the string
# if we dont enter any value at the palce of m it will defaulty be 0 and for n's default is the len() of string.
''' Also to access the strings specific character we use the numeric indexes of the string'''
print(a[0]) # This is to print the first character of the string
print(a[-1]) # This is to print the last character of the string
#they also contain reverse indexing too which starts from -1

print(c[0:15:4])
# This is to print the string from 0 to 5th index with a step of 2
# step of 2 of any other number means that it will print 0th  element 
# then skip next two and print the next then again skip two element and print till string is finished



