def is_same_class(obj, a_class):
    # Use isinstance check with strict comparison
    return isinstance(obj, a_class) and obj.__class__ == a_class

a = 1
is_printed = False
if is_same_class(a, int):
    is_printed = True
    print(f"{a} is an exact instance of the class {int.__name__}")

# Additional checks with other classes
if is_same_class(a, float) or is_same_class(a, object):
    # Handle other cases or print nothing if not applicable

    if not is_printed:
    print(f"{a} is not an exact instance of any specified class")

# Output: 1 is an exact instance of the class int
