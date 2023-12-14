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

def is_same_class(obj, a_class):
    return isinstance(obj, a_class) and obj.__class__ == a_class


