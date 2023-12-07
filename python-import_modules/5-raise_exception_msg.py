def raise_exception_msg(message=""):
  """
  Raises a NameError exception with a custom message.

  Args:
    message: The custom message to include in the exception.
  """
  raise NameError(f"This is a custom name exception: {message}")