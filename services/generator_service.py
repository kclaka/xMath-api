from services.helper_service import random_number, finding_divisor

class Generator:
    @staticmethod
    def addition(max_first: int, min_first: int, max_second: int, min_second: int) -> dict:
        first = random_number(min_first, max_first)
        second = random_number(min_second, max_second)
        operation = "+"
        expression = f"{first} {operation} {second}"
        answer = first + second

        return {"first": first, "second": second, "operation": operation, "expression": expression, "answer": answer}

    @staticmethod
    def subtraction(max_first: int, min_first: int, max_second: int, min_second: int, allow_negative: bool = True) -> dict:
        first = random_number(min_first, max_first)
        second = random_number(min_second, max_second)

        if first < second and not allow_negative:
            first, second = second, first

        operation = "-"
        expression = f"{first} {operation} {second}"
        answer = first - second

        return {"first": first, "second": second, "operation": operation, "expression": expression, "answer": answer}

    @staticmethod
    def multiplication(max_first: int, min_first: int, max_second: int, min_second: int) -> dict:
        first = random_number(min_first, max_first)
        second = random_number(min_second, max_second)
        operation = "*"
        expression = f"{first} {operation} {second}"
        answer = first * second

        return {"first": first, "second": second, "operation": operation, "expression": expression, "answer": answer}

    @staticmethod
    def division(max_first: int, min_first: int) -> dict:
        first = random_number(min_first, max_first)
        second = finding_divisor(first) or 1  # Ensure second is not zero
        operation = "/"
        expression = f"{first} {operation} {second}"
        answer = first / second

        return {"first": first, "second": second, "operation": operation, "expression": expression, "answer": answer}

    @staticmethod
    def random_operation(max_first: int, min_first: int, max_second: int, min_second: int, allow_negative: bool = True) -> dict:
        n = random_number(1, 4)
        if n == 1:
            return Generator.addition(max_first, min_first, max_second, min_second)
        elif n == 2:
            return Generator.subtraction(max_first, min_first, max_second, min_second, allow_negative)
        elif n == 3:
            return Generator.multiplication(max_first, min_first, max_second, min_second)
        elif n == 4:
            return Generator.division(max_first, min_first)
        else:
            raise ValueError("Invalid operation choice")

# Export an instance of the Generator class
generator = Generator()
