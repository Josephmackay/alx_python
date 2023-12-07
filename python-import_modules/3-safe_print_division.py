def safe_print_division(a, b):
    try:
        result = a / b
    except b == 0:
        print("Inside result: None")
        print("{} = None".format(result))
        return None
    finally:
        print("Inside result: {}".format(result))
    return result