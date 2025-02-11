# Property Decorator and Operator Overloading in Python
# - Property decorators allow us to manage the access and modification of an object's attributes
#   through getter, setter, and deleter methods. It is a way of controlling how attributes are 
#   accessed or modified without needing direct calls to methods.
# - Operator overloading lets us redefine the behavior of standard operators such as +, -, *, etc.,
#   to work with our custom classes and provide a more intuitive syntax.

class Rectangle:
    """A class to represent a rectangle with property decorators and operator overloading."""

    # Constructor for initializing object attributes (length and width).
    # Length and width will be set as private attributes (_length and _width).
    def __init__(self, length, width):
        """
        Initialize the rectangle object with a specified length and width.

        Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        """
        self._length = length  # The length of the rectangle (private attribute).
        self._width = width    # The width of the rectangle (private attribute).
        
    # Getter and Setter for length using @property and @<property_name>.setter.

    @property
    def length(self):
        """
        Getter method for the length property. This returns the current value of the length.
        The method is decorated with @property to make it behave like an attribute.

        Returns:
        float: The length of the rectangle.
        """
        return self._length  # Simply returns the value stored in the private attribute _length.

    @length.setter
    def length(self, value):
        """
        Setter method for the length property. This ensures the length is positive when setting it.
        The method is decorated with @<property_name>.setter to modify the value of the length.

        Parameters:
        value (float): The new value for the length of the rectangle.
        """
        if value > 0:
            self._length = value  # Assign the new positive value to the private attribute _length.
        else:
            print("Length must be a positive value.")  # Validate that the length is positive.

    @property
    def width(self):
        """
        Getter method for the width property. This returns the current value of the width.
        The method is decorated with @property to make it behave like an attribute.

        Returns:
        float: The width of the rectangle.
        """
        return self._width  # Simply returns the value stored in the private attribute _width.

    @width.setter
    def width(self, value):
        """
        Setter method for the width property. This ensures the width is positive when setting it.
        The method is decorated with @<property_name>.setter to modify the value of the width.

        Parameters:
        value (float): The new value for the width of the rectangle.
        """
        if value > 0:
            self._width = value  # Assign the new positive value to the private attribute _width.
        else:
            print("Width must be a positive value.")  # Validate that the width is positive.

    # Read-Only Property for calculating the area of the rectangle.
    @property
    def area(self):
        """
        Calculate and return the area of the rectangle. This property only has a getter, so it's read-only.
        The area is calculated using the formula: area = length * width.

        Returns:
        float: The area of the rectangle.
        """
        return self._length * self._width  # The area is the product of length and width.

    # Operator Overloading: Overloading the addition operator (+) to add two rectangles based on their areas.
    def __add__(self, other):
        """
        Overload the + operator to add the areas of two rectangles and create a new rectangle based on the 
        summed areas. The new rectangle's dimensions are derived by approximating square-like proportions.

        Parameters:
        other (Rectangle): Another Rectangle object to add to the current one.

        Returns:
        Rectangle: A new Rectangle object with a length and width that represent the combined area.
        """
        if isinstance(other, Rectangle):  # Check if the other object is also a Rectangle.
            # Sum the areas of both rectangles.
            new_area = self.area + other.area
            # Calculate new dimensions for the resulting rectangle based on the combined area.
            new_length = (new_area) ** 0.5  # Calculate the square root of the area to get a "length".
            new_width = new_length  # Assuming the resulting rectangle is square-like.
            return Rectangle(new_length, new_width)  # Return a new Rectangle with these dimensions.
        else:
            raise ValueError("Cannot add non-Rectangle object.")  # Ensure that we only add Rectangle objects.

    # Operator Overloading: Overloading the subtraction operator (-) to subtract areas of two rectangles.
    def __sub__(self, other):
        """
        Overload the - operator to subtract the area of one rectangle from another, resulting in a new rectangle.
        The new rectangle will have the dimensions derived from the difference in areas.

        Parameters:
        other (Rectangle): Another Rectangle object to subtract from the current one.

        Returns:
        Rectangle: A new Rectangle object with dimensions derived from the difference in areas.
        """
        if isinstance(other, Rectangle):  # Check if the other object is a Rectangle.
            new_area = self.area - other.area  # Subtract the area of the other rectangle from this rectangle.
            if new_area > 0:  # Ensure the resulting area is positive before creating a new rectangle.
                new_length = new_area ** 0.5  # Calculate the square root of the new area for length.
                new_width = new_length  # Assuming the resulting rectangle is square-like.
                return Rectangle(new_length, new_width)  # Return a new Rectangle with the new dimensions.
            else:
                raise ValueError("Resulting area is negative, cannot create a rectangle.")  # Handle negative areas.
        else:
            raise ValueError("Cannot subtract non-Rectangle object.")  # Ensure that we only subtract Rectangle objects.

    # Overload the __str__ method to provide a user-friendly string representation of the rectangle.
    def __str__(self):
        """
        Overload the __str__ method to return a string representation of the rectangle's dimensions and area.
        This method is called when the object is printed or converted to a string.

        Returns:
        str: A string that describes the rectangle's dimensions and area.
        """
        return f"Rectangle: Length = {self.length}, Width = {self.width}, Area = {self.area}"

# Example Usage:

# Create two rectangle objects with length and width.
rect1 = Rectangle(5, 3)  # Rectangle 1 with length 5 and width 3.
rect2 = Rectangle(4, 2)  # Rectangle 2 with length 4 and width 2.

# Accessing the area property directly:
print(f"Area of Rectangle 1: {rect1.area}")  # Output: 15 (5 * 3)
print(f"Area of Rectangle 2: {rect2.area}")  # Output: 8 (4 * 2)

# Access and modify the length and width using getter and setter methods.
rect1.length = 6  # Set a new valid length for Rectangle 1.
rect1.width = 4   # Set a new valid width for Rectangle 1.
print(f"Updated Rectangle 1: {rect1}")  # Output: Rectangle: Length = 6, Width = 4, Area = 24

# Using overloaded `+` operator to add two rectangles.
rect3 = rect1 + rect2  # Add the areas of rect1 and rect2 to create a new rectangle.
print(f"Rectangle 3 (Sum of rect1 and rect2): {rect3}")  # Output: New rectangle based on summed areas.

# Using overloaded `-` operator to subtract two rectangles.
rect4 = rect1 - rect2  # Subtract the area of rect2 from rect1 to create a new rectangle.
print(f"Rectangle 4 (Difference of rect1 and rect2): {rect4}")  # Output depends on the areas of rect1 and rect2.

# Example of invalid operation: trying to add a Rectangle object to a non-Rectangle object.
try:
    result = rect1 + "Not a rectangle"
except ValueError as e:
    print(e)  # Output: Cannot add non-Rectangle object.

# Example of invalid operation: trying to subtract a non-Rectangle object.
try:
    result = rect1 - "Not a rectangle"
except ValueError as e:
    print(e)  # Output: Cannot subtract non-Rectangle object.
