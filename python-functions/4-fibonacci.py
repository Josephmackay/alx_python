def fibonacci_sequence(n):
    if n < 0:
        raise ValueError([])

    sequence = []
    if n == 0:
        return sequence
    elif n == 1:
        sequence.append(0)
        return sequence
    elif n == 2:
        sequence.extend([0, 1])
        return sequence
    else:
        sequence.extend([0, 1])
        for _ in range(2, n):
            next_number = sequence[-1] + sequence[-2]
            # Check for overflow
            if next_number < 0:
                raise OverflowError("Fibonacci sequence overflow")
            sequence.append(next_number)
        return sequence