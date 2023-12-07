def multiply_list_map(my_list=[], number=0):
  """
  Returns a new list with all values multiplied by a number.

  Args:
    my_list: The list to process.
    number: The number to multiply each element by.

  Returns:
    A new list with the multiplied values.
  """
  return list(map(lambda x: x * number, my_list))