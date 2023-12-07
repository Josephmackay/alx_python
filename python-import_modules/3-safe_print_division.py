def safe_print_division(a, b):
  """
  Divides two integers and prints the result safely.

  Args:
    a: The first integer to be divided.
    b: The second integer to be divided by.

  Returns:
    The result of the division or None if an error occurs.
  """
  try:
    result = a / b
    print(f"Inside result: {result}")
  except ZeroDivisionError:
    print("Error: Division by zero")
    return None
  finally:
    return result
