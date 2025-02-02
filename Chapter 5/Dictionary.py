# Dictionaries are key-value pairs used to store data in Python.
# Keys must be unique and immutable, while values can be of any data type.

# Defining a dictionary
my_dict = {
    "name": "Alice",
    "age": 24,
    "city": "London",
    "skills": ["Python", "Machine Learning"],
}
print(my_dict)  # Output: {'name': 'Alice', 'age': 24, 'city': 'London', 'skills': ['Python', 'Machine Learning']}

# Accessing values using keys
# Square brackets [key] directly fetch the value for the given key.
print(my_dict["name"])  # Output: Alice

# Using the get() method to access a value
# get() safely retrieves a value without throwing an error if the key is missing.
# You can provide a default value to return if the key doesn't exist.
print(my_dict.get("age"))  # Output: 24
print(my_dict.get("country", "Not Found"))  # Output: Not Found (default value for missing key)

# Adding or updating key-value pairs
# Adding: If the key doesn't exist, it creates a new key-value pair.
my_dict["country"] = "UK"
print(my_dict)  # Output: {'name': 'Alice', 'age': 24, 'city': 'London', 'skills': ['Python', 'Machine Learning'], 'country': 'UK'}

# Updating: If the key exists, it updates the value.
my_dict["age"] = 25
print(my_dict["age"])  # Output: 25

# Using the update() method to merge or modify dictionaries
# update() allows you to add or modify multiple key-value pairs at once.
additional_data = {"profession": "Engineer", "hobbies": ["Reading", "Traveling"]}
my_dict.update(additional_data)
print(my_dict)  
# Output: {'name': 'Alice', 'age': 25, 'city': 'London', 'skills': ['Python', 'Machine Learning'], 'country': 'UK', 'profession': 'Engineer', 'hobbies': ['Reading', 'Traveling']}

# Viewing all keys in the dictionary
# keys() returns a view object containing all the keys in the dictionary.
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city', 'skills', 'country', 'profession', 'hobbies'])

# Viewing all values in the dictionary
# values() returns a view object containing all the values in the dictionary.
print(my_dict.values())  # Output: dict_values(['Alice', 25, 'London', ['Python', 'Machine Learning'], 'UK', 'Engineer', ['Reading', 'Traveling']])

# Viewing all key-value pairs
# items() returns a view object of key-value pairs as tuples.
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 25
# city: London
# skills: ['Python', 'Machine Learning']
# country: UK
# profession: Engineer
# hobbies: ['Reading', 'Traveling']

# Removing a key-value pair using pop()
# pop(key) removes the specified key and returns its value.
removed_value = my_dict.pop("city")
print(removed_value)  # Output: London
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'skills': ['Python', 'Machine Learning'], 'country': 'UK', 'profession': 'Engineer', 'hobbies': ['Reading', 'Traveling']}

# Removing the last inserted key-value pair using popitem()
# popitem() removes and returns the last key-value pair as a tuple.
last_item = my_dict.popitem()
print(last_item)  # Output: ('hobbies', ['Reading', 'Traveling'])
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'skills': ['Python', 'Machine Learning'], 'country': 'UK', 'profession': 'Engineer'}

# Checking if a key exists using "in"
# "in" checks for the presence of a key in the dictionary.
print("skills" in my_dict)  # Output: True
print("hobbies" in my_dict)  # Output: False

# Clearing all key-value pairs
# clear() removes everything from the dictionary, making it empty.
my_dict.clear()
print(my_dict)  # Output: {}

# Copying a dictionary
# copy() creates a shallow copy of the dictionary.
original_dict = {"x": 1, "y": 2, "z": 3}
copied_dict = original_dict.copy()
print(copied_dict)  # Output: {'x': 1, 'y': 2, 'z': 3}

# Merging two dictionaries using |
# | merges two dictionaries, with values from the second one overwriting duplicates.
dict1 = {"a": 10, "b": 20}
dict2 = {"b": 30, "c": 40}
merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 10, 'b': 30, 'c': 40}
