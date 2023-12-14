def is_same_class(obj, a_class):
    return type(obj) is a_class

is_same_class(1, int)    # True
is_same_class(1, object) # False

# Example usage
a=1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
elif is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
else:
    print("{} is an instance of the class {}".format(a, object.__name__))
