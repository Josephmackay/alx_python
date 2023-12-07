def best_score(a_dictionary):
  """
  Returns the key with the biggest integer value in a dictionary.

  Args:
    a_dictionary: The dictionary to process.

  Returns:
    The key with the biggest integer value, or None if no score found.
  """
  if not a_dictionary:
    return None
  best_key = max(a_dictionary, key=a_dictionary.get)
  return best_key