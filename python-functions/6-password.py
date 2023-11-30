def validate_password(password):
    if len(password) < 8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_space = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char == " ":
            has_space = True

    if not has_uppercase:
        return False

    if not has_lowercase:
        return False

    if not has_digit:
        return False

    if has_space:
        return False

    return True