# Classes in Python:
# - A class is a template or blueprint that defines the attributes (variables) and behaviors (methods) of objects.
# - Objects are instances of a class, with their own data and methods to perform actions.
# - We define classes using the `class` keyword, followed by the class name, which follows the PascalCase convention.

class Animal:
    """A class to represent animals with a name, sound, and species."""

    # Class Attributes:
    # - Class attributes are shared across all instances (objects) of a class.
    # - These attributes are defined directly inside the class, outside any methods.
    # - Class attributes are accessed using the class name, and they are the same for all objects unless overridden.
    
    # Input from the user to set class attributes for the species
    species_1 = input("Enter the first species of Animal: ")  # Shared attribute for all instances
    species_2 = input("Enter the second species of Animal: ")  # Another shared attribute for all instances

    # Constructor Method (__init__):
    # - The __init__() method is a special method that is automatically called when we create an object of the class.
    # - It initializes (sets) the object's specific data (instance attributes).
    # - The parameters 'name' and 'sound' will be passed when creating an object, and they are used to initialize the instance variables.
    def __init__(self, name, sound):
        """
        Initialize an object with a name and sound.
        
        Parameters:
        name (str): The name of the animal.
        sound (str): The sound the animal makes.
        """
        # The 'self' keyword refers to the current instance of the class.
        # It allows access to the instance's attributes (specific to this object) and methods.
        self.name = name  # Instance attribute for the animal's name.
        self.sound = sound  # Instance attribute for the animal's sound.

    # Instance Methods:
    # - Instance methods are functions that operate on data specific to an instance of the class.
    # - They always take 'self' as the first parameter to access instance variables and methods.
    
    def make_sound(self):
        """
        Print the sound made by the animal.
        This method accesses the 'name' and 'sound' attributes of the object.
        """
        # Accessing instance attributes (self.name and self.sound) to print the sound made by the specific animal object.
        print(f"{self.name} makes the sound: {self.sound}")

    # Combining Instance and Class Attributes:
    # - This method accesses both the instance attributes (like 'name', 'sound') and class attributes (like species_1 and species_2).
    def display_info(self):
        """
        Print information about the object and the shared class attributes.
        Combines instance-specific data with class-level shared attributes.
        """
        # Access both the class attributes 'species_1' and 'species_2' as well as instance-specific attributes ('name' and 'sound').
        print(
            f"Animal Name: {self.name}, Species 1: {self.species_1}, Sound: {self.sound}\n"
            f"Animal Name: {self.name}, Species 2: {self.species_2}, Sound: {self.sound}"
        )

    # Static Methods:
    # - Static methods are not dependent on the instance or class attributes.
    # - They are independent and usually serve as utility methods that perform actions related to the class.
    # - Static methods are defined using the @staticmethod decorator.
    
    @staticmethod
    def general_info():
        """
        Provide general information about animals.
        This method does not access any instance or class-specific data.
        """
        # This method simply prints general information about animals, independent of any object.
        print("Animals are multicellular organisms that belong to the kingdom Animalia.")

    # Dunder Method (`__str__`):
    # - The `__str__` method is a special method that defines how an object is represented as a string.
    # - It is automatically called when we use `print()` or `str()` on an object.
    # - It returns a string that represents the object in a readable way.
    def __str__(self):
        """
        Return a readable string representation of the object.
        Shows the object's name, species, and sound.
        """
        # This method provides a string representation of the object that is easy to understand.
        # It returns a string with the animal's name, species (class attribute), and the sound.
        return f"Animal(Name: {self.name}, Species: {self.species_1}, Sound: {self.sound})"


# Object Creation:
# - Objects are created by calling the class as if it were a function and passing the required arguments to the constructor.
# - The constructor method `__init__` is automatically called when an object is instantiated.

# Creating objects (instances) of the Animal class.
dog = Animal("Dog", "Bark")  # Creating an instance of the Animal class for a dog.
cat = Animal("Cat", "Meow")  # Creating an instance of the Animal class for a cat.

# Accessing Instance Methods:
# - Instance methods work on the data specific to an individual object.
# - We use the object name to call an instance method.

dog.make_sound()  # Output: Dog makes the sound: Bark
cat.make_sound()  # Output: Cat makes the sound: Meow

# Accessing Instance and Class Attributes:
# - Instance attributes belong to individual objects and are accessed through the 'self' reference (e.g., `self.name`).
# - Class attributes are shared across all objects of the class and are accessed using the class name (e.g., `Animal.species_1`).

dog.display_info()  # This will print information including the shared species attributes and specific dog info.
cat.display_info()  # This will print information including the shared species attributes and specific cat info.

# Using Static Methods:
# - Static methods are general-purpose and not tied to any specific instance of the class.
# - They can be called using either the class name or an object, though it's more common to use the class name.
# - Static methods do not have access to instance attributes (`self`) or class attributes (`cls`).

Animal.general_info()  # Output: Animals are multicellular organisms in the kingdom Animalia.
dog.general_info()     # Same output, but better practice to call it through the class name.

# Using the Dunder (`__str__`) Method:
# - The `__str__` method defines how an object is converted to a string.
# - It's automatically used when you use the `print()` function on an object.
# - It provides a human-readable string representation of the object.

print(dog)  # Output: Animal(Name: Dog, Species: <species_1_input>, Sound: Bark)
print(cat)  # Output: Animal(Name: Cat, Species: <species_2_input>, Sound: Meow)

# Summary:
# - Classes in Python encapsulate data and methods that define behaviors for objects.
# - `__init__` is used to initialize objects, and instance attributes are unique to each object.
# - Class attributes are shared by all objects, and static methods are independent of any specific object.
# - Dunder methods like `__str__` are used to customize object behavior for common operations like printing.
# - This code demonstrates various concepts in object-oriented programming (OOP) including inheritance, methods, attributes, and static methods.
