def is_same_class(obj, a_class):
    # Use isinstance check with strict comparison
    return isinstance(obj, a_class) and obj.__class__ == a_class

# Example usage
a = 1
if is_same_class(a, int):
    print("{} is an exact instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an exact instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an exact instance of the class {}".format(a, object.__name__))
    
# Output
print("{} is an exact instance of the class {}".format(a, int.__name__))
