"""
This function checks if an object is an exact instance of a specified class without importing any external modules.

Args:
    obj: The object to be checked.
    a_class: The class to compare against.

Returns:
    True if the object is an exact instance of the class, False otherwise.

Examples:
    ```python
    is_same_class(1, int)  # True
    is_same_class([], list)  # True
    is_same_class("string", str)  # True
    is_same_class(1.0, float)  # False (not exact class match)
    is_same_class([], tuple)  # False (subclass, not exact match)
    ```
"""
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        return self.__size

    def area(self):
        return self.__size**2

    def perimeter(self):
        return 4 * self.__size

    def __str__(self):
        return f"Square with size: {self.__size}"

    def __repr__(self):
        return f"Square({self.__size})"
    
my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

