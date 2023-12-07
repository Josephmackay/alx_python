def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        print("{} = None".format(result))
        return None
    finally:
        print("Inside result: {}".format(result))
    return result