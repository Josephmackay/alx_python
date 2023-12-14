def is_same_class(obj, a_class):
    # Use isinstance check with strict comparison
    return isinstance(obj, a_class) and obj.__class__ == a_class


# Output
print("{} is an exact instance of the class {}".format(a, int.__name__))
