def multiple_returns(sentence):
  """
  Returns a tuple containing the length of a string and its first character.

  Args:
    sentence: The string to process.

  Returns:
    A tuple containing (length, first_character).
  """
  length = len(sentence)
  first_character = sentence[0] if sentence else None
  return (length, first_character)