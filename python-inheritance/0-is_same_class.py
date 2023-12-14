def is_same_class(obj, a_class):
    return type(obj) is a_class

is_same_class(1, int)    # True
is_same_class(1, object) # False

# Example usage

