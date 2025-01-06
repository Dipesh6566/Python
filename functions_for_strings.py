a = '''This is the file created by Dipesh'''
#there is a upper() function in python which converts the string to upper case
#there is a lower() function in python which converts the string to lower case
print(a.upper()) # This is to convert the string to upper case
print(a.lower()) # This is to convert the string to lower case
print(a.endswith("sh"))
#there is a endswith() function in python 
# which checks if the string ends with the given part provided in function
print(a.startswith("This"))
#there is a startswith() function in python
# which checks if the string starts with the given part provided in function
print(a.replace("Dipesh", "Dip")) # This is to replace the string with
#there is a replace() function in python
# which replaces the string with the given part provided in function
# the first part is the string we want to change and
# second is with which we want to change the first part in the rwplace function
#there is a split() function in python which splits the string into a list of words
print(a.split(" ")) # This is to split the string into a list of words
#there is a join() function in python which joins the list of words into a string
print(" ".join(a.split(" "))) # This is to join the list of words into a string
#there is a strip() function in python which removes the leading and trailing spaces from the string
print(a.strip()) # This is to remove the leading and trailing spaces from the string
#In Python, the method strip() is used to remove 
# any leading (at the beginning) and trailing (at the end) 
# whitespace characters or specified characters from a string
#there is a find() function in python which returns the index of the first occurrence of the specified
# value in the string
print(a.find("Dip")) # This is to find the index of the first occurrence of the
# passed value in the function
#there is a rfind() function in python which returns the highest index of the specified value
# in the string
print(a.rfind("Dip")) # This is to find the highest index of the specified value
#there is a count() function in python which returns the number of occurrences of the specified value in
# the string
print(a.count("Dip")) # This is to find the number of occurrences of the specified value
#there is a isalnum() function in python which returns True if all characters in the string are
# alphanumeric, meaning alphabet letter (a-z) and numerals (0-9)
print(a.isalnum()) # This is to check if all characters in the string are alphanumeric
#there is a isalpha() function in python which returns True if all characters in the string are
# alphabet letter (a-z)
print(a.isalpha()) # This is to check if all characters in the string are alphabet letter
#there is a isdigit() function in python which returns True if all characters in the string are
# numerals (0-9)
print(a.isdigit()) # This is to check if all characters in the string are numerals
#there is a islower() function in python which returns True if all cased characters in the
# string are lowercase and there is at least one cased character, otherwise False
print(a.islower()) # This is to check if all cased characters in the string are lowercase
#there is a isupper() function in python which returns True if all cased characters in the
# string are uppercase and there is at least one cased character, otherwise False
print(a.isspace()) # This is to check if all characters in the string are whitespace characters
#there is a isprintable() function in python which returns True if all characters in the string
# are printable, otherwise False
print(a.isprintable()) # This is to check if all characters in the string are printable






