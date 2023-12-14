def is_same_class(obj, a_class):
  """
  Checks if an object is an exact instance of a specified class.

  Args:
    obj: The object to be checked.
    a_class: The class to compare against.

  Returns:
    True if the object is an exact instance of the class, False otherwise.
  """
  # Use isinstance with strict comparison to check the object type.
  # Then, compare their internal classes to ensure exact match.
  return isinstance(obj, a_class) and obj.__class__ == a_class

# Example usage
a = 1
