def common_elements(set_1, set_2):
  """
  Returns the set of common elements between two sets.

  Args:
    set_1: The first set.
    set_2: The second set.

  Returns:
    A set containing the common elements.
  """
  common_elements = set()
  for element in set_1:
    if element in set_2:
      common_elements.add(element)
  return common_elements