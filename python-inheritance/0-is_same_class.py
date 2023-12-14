def is_same_class(obj, a_class):
    # Use isinstance check with strict comparison
    if isinstance(obj, a_class) and obj.__class__ == a_class:
        return True
    else:
        return False

