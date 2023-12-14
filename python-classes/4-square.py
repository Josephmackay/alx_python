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
        self.__size = size  # Initialize private attribute

    @property
    def size(self):
        return self.__size  # Getter for size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Setter with validation

    def area(self):
        return self.__size**2

    def __str__(self):
        return f"Square with size: {self.__size}"

    def __repr__(self):
        return f"Square({self.__size})"

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

