import random

def random_number(min_value: int, max_value: int) -> int:
    """
    Generate a random number between min_value and max_value (inclusive).

    :param min_value: Minimum value
    :param max_value: Maximum value
    :return: Random integer
    """
    return random.randint(min_value, max_value)

def finding_divisor(number: int) -> int:
    """
    Find a random divisor of the given number.

    :param number: The number to find a divisor for
    :return: A random divisor of the number
    """
    divisors = []

    if number < 0:
        for i in range(number, 0):  # Negative range up to zero
            if number % i == 0:
                divisors.append(i)
                divisors.append(-i)
    else:
        for i in range(1, number + 1):  # Positive range starting from 1
            if number % i == 0:
                divisors.append(i)

    if len(divisors) > 1:
        return divisors[random_number(1, len(divisors) - 2)]
    return divisors[0] if divisors else None
