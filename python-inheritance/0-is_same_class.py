def is_same_class(obj, a_class):
    # Use isinstance check with strict comparison
    return isinstance(obj, a_class) and obj.__class__ == a_class

a = 1
if is_same_class(a, int):
    print(True/False)


# Output: 1 is an exact instance of the class int
