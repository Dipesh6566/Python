# Parent Class: Employee
class Employee:
    # Class variable (Shared among all instances of the class)
    # The 'company' attribute is a class-level variable that is common to all instances of the Employee class.
    # All employees will belong to the same company unless overridden in a subclass.
    # It is defined outside of the __init__() method, meaning it's not tied to any specific instance, but shared by all instances.
    # This will allow any object of type Employee or its subclasses to reference the same 'company' name.
    company = "ITC"  # Company is the name of the company all employees work for by default.
    
    def __init__(self, name, salary):
        # Instance variables (Specific to each object)
        # 'name' and 'salary' are instance variables. This means each employee object will store its own unique name and salary.
        # They are passed to the __init__() method when creating an instance of the Employee class.
        # 'self' refers to the instance of the object being created. The instance variables are assigned values specific to each object.
        
        self.name = name  # 'name' holds the name of the employee. It is specific to this instance, so each employee can have their own name.
        self.salary = salary  # 'salary' holds the salary of the employee. This is also specific to each instance, so each employee can have a different salary.
    
    def show(self):
        # This method is used to display the basic details of the employee.
        # It accesses the instance variables 'name', 'salary', and the class variable 'company' to print employee details.
        # The 'self' keyword is used to access the instance variables (such as name and salary) of the current object (instance) on which the method is called.
        
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company}")
        # This prints out the employee's name, salary, and the company they work for.
        # The company value is taken from the class variable, which is shared by all instances of the class.
    
    @classmethod
    def company_info(cls):
        # This is a class method. It is bound to the class, not the instance.
        # The 'cls' keyword refers to the class itself (Employee), not the instance of the class.
        # Class methods can access and modify class variables, which are shared across all instances of the class.
        
        print(f"Company: {cls.company}")
        # This prints the name of the company by accessing the class variable 'company'.
        # This method does not require any object to be called, and can be called directly on the class itself.
        # It's used to print company information for all employees.

# Child Class: Programmer (inherits from Employee)
class Programmer(Employee):
    # Class variable (Overridden from the parent class)
    # The 'company' attribute is redefined in the Programmer class to represent a different company name for this subclass.
    # Any instance of the Programmer class will have "Info_Tech" as the company, unless explicitly overridden in an object.
    company = "Info_Tech"
    
    def __init__(self, name, salary, language):
        # The __init__() method is used to initialize a new object of the Programmer class.
        # 'name' and 'salary' are passed to the parent (Employee) class's __init__ method using the 'super()' function.
        # This ensures that 'name' and 'salary' are properly initialized for all Employee objects (inherited by Programmer).
        # Additionally, 'language' is a new attribute specific to the Programmer class, representing the programming language the programmer knows.
        
        super().__init__(name, salary)  # Calls the __init__() method of the parent class (Employee) to initialize 'name' and 'salary'.
        self.language = language  # 'language' is an instance variable specific to Programmer, storing the programming language (e.g., Python).
    
    def show_language(self):
        # This method is specific to the Programmer class. It displays the name of the programmer and the programming language they know.
        # It accesses the instance variables 'name' and 'language' to display this information for the specific programmer object.
        
        print(f"Programmer Name: {self.name}, Programming Language: {self.language}")
        # This prints out the name of the programmer and the programming language they specialize in.
        # The 'name' is inherited from the Employee class, and 'language' is specific to the Programmer class.

    @classmethod
    def company_info(cls):
        # This is an overridden class method in the Programmer class.
        # It replaces the 'company_info' method from the Employee class. Now, it prints the company for the Programmer class.
        # Since 'company' was overridden in the Programmer class, this method prints the programmer's company name ("Info_Tech").
        
        print(f"Programmer Company: {cls.company}")
        # This prints the company information using the class variable 'company' from the Programmer class.
        # This ensures that any Programmer object will use "Info_Tech" as the company, even if Employee class has a different value for 'company'.
        
# Types of Inheritance (for explanation)
# Inheritance is the ability of a class (child class) to inherit attributes and methods from another class (parent class).
# It allows for code reuse, reduces redundancy, and supports a hierarchical class structure.
# There are several types of inheritance:
# - **Single Inheritance:** A class inherits from a single parent class.
# - **Multiple Inheritance:** A class inherits from multiple parent classes.
# - **Multilevel Inheritance:** A class inherits from another class, which in turn inherits from another class.
# - **Hierarchical Inheritance:** Multiple classes inherit from a single parent class.
# - **Hybrid Inheritance:** A mix of two or more inheritance types.

# 1. **Single Inheritance**: A class inherits from only one parent class.
#    Example: `Programmer` inherits from `Employee`. This is the most straightforward form of inheritance.
#    The child class gets access to methods and attributes of the single parent class.

# 2. **Multiple Inheritance**: A class can inherit from multiple parent classes.
#    Example: A class `Manager` could inherit from both `Employee` and `Leader`.
#    The child class inherits attributes and methods from all its parent classes, combining behaviors from multiple sources.

# 3. **Multilevel Inheritance**: A class can inherit from another class, which itself inherits from another class.
#    Example: `SeniorProgrammer` inherits from `Programmer`, which inherits from `Employee`.
#    This forms a chain of inheritance, where the child class gets attributes and methods from all its ancestors.

# 4. **Hierarchical Inheritance**: Multiple subclasses inherit from a single parent class.
#    Example: Both `Programmer` and `Manager` could inherit from `Employee`.
#    This allows different child classes to share common functionality from a single parent class.

# 5. **Hybrid Inheritance**: A combination of two or more inheritance types (e.g., multilevel and multiple inheritance).
#    Example: A class `SpecialEmployee` might inherit from both `Manager` and `Programmer`.

# Example of Multiple Inheritance:
class Manager(Employee):
    # Manager class inherits from Employee, and can have additional methods or properties specific to managers.
    def __init__(self, name, salary, department):
        # The __init__ method initializes the 'name' and 'salary' using the parent class constructor.
        # The 'department' attribute is new for the Manager class, representing the department managed by the manager.
        
        super().__init__(name, salary)  # Calls the __init__() method from Employee class to initialize 'name' and 'salary'.
        self.department = department  # 'department' is a new instance variable specific to Manager class.
    
    def show_department(self):
        # This method displays the department in which the manager works.
        # It accesses the 'name' and 'department' attributes specific to the Manager class.
        
        print(f"Manager Name: {self.name}, Department: {self.department}")
        # It prints the name of the manager and the department they manage.

# Example of Multilevel Inheritance:
class SeniorProgrammer(Programmer):
    # SeniorProgrammer inherits from Programmer, which itself inherits from Employee.
    # This allows SeniorProgrammer to have all attributes and methods from both Programmer and Employee.
    
    def __init__(self, name, salary, language, experience):
        # The __init__ method initializes 'name', 'salary', and 'language' by calling the parent class constructors.
        # It also adds 'experience' as a new attribute to represent how many years of experience the senior programmer has.
        
        super().__init__(name, salary, language)  # Initializes 'name', 'salary', and 'language' using the Programmer constructor.
        self.experience = experience  # 'experience' is a new attribute specific to SeniorProgrammer, representing years of experience.
    
    def show_experience(self):
        # This method displays the experience level of the SeniorProgrammer.
        # It accesses the 'name' and 'experience' attributes specific to the SeniorProgrammer class.
        
        print(f"Senior Programmer Name: {self.name}, Experience: {self.experience} years")
        # It prints the name and the experience of the senior programmer.

# Example usage:

# Creating an instance of the Employee class
emp = Employee("John", 50000)  # Creates an employee named John with a salary of 50,000.
emp.show()  # Prints the basic employee information (name, salary, company).

# Creating an instance of the Programmer class
prog = Programmer("Alice", 60000, "Python")  # Creates a programmer named Alice who knows Python with a salary of 60,000.
prog.show()  # Prints the employee information (inherited from Employee class).
prog.show_language()  # Prints the programming language known by Alice.

# Creating an instance of the Manager class
mgr = Manager("Bob", 70000, "HR")  # Creates a manager named Bob with a salary of 70,000 who manages the HR department.
mgr.show()  # Prints the employee information (inherited from Employee class).
mgr.show_department()  # Prints the department managed by Bob.

# Creating an instance of the SeniorProgrammer class
sen_prog = SeniorProgrammer("Eve", 80000, "Java", 5)  # Creates a senior programmer named Eve with 5 years of experience in Java.
sen_prog.show()  # Prints the employee information (inherited from Employee class).
sen_prog.show_language()  # Prints the programming language known by Eve.
sen_prog.show_experience()  # Prints Eve's years of experience.
