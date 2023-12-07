def print_matrix_integer(matrix=[[]]):
  """
  Prints a matrix of integers.

  Args:
    matrix: A list of lists containing integers.
  """
  for row in matrix:
    for i, num in enumerate(row):
      print("{:d}".format(num), end="")
      if i < len(row) - 1:
        print(" ", end="")
    print("")