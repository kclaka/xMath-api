from flask import request, jsonify
from services.generator_service import generator
import random

DEFAULT_MAX = 99
DEFAULT_MIN = 1

class GeneratorController:
    @staticmethod
    def addition():
        try:
            max_val = int(request.args.get("max", DEFAULT_MAX))
            min_val = int(request.args.get("min", DEFAULT_MIN))
            max_first = int(request.args.get("maxFirst", max_val))
            min_first = int(request.args.get("minFirst", min_val))
            max_second = int(request.args.get("maxSecond", max_val))
            min_second = int(request.args.get("minSecond", min_val))

            expression = generator.addition(max_first, min_first, max_second, min_second)
            return jsonify(expression)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def subtraction():
        try:
            max_val = int(request.args.get("max", DEFAULT_MAX))
            min_val = int(request.args.get("min", DEFAULT_MIN))
            max_first = int(request.args.get("maxFirst", max_val))
            min_first = int(request.args.get("minFirst", min_val))
            max_second = int(request.args.get("maxSecond", max_val))
            min_second = int(request.args.get("minSecond", min_val))
            negative = bool(int(request.args.get("negative", 0)))

            expression = generator.subtraction(max_first, min_first, max_second, min_second, negative)
            return jsonify(expression)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def multiplication():
        try:
            max_val = int(request.args.get("max", DEFAULT_MAX))
            min_val = int(request.args.get("min", DEFAULT_MIN))
            max_first = int(request.args.get("maxFirst", max_val))
            min_first = int(request.args.get("minFirst", min_val))
            max_second = int(request.args.get("maxSecond", max_val))
            min_second = int(request.args.get("minSecond", min_val))

            expression = generator.multiplication(max_first, min_first, max_second, min_second)
            return jsonify(expression)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def division():
        try:
            max_val = int(request.args.get("max", DEFAULT_MAX))
            min_val = int(request.args.get("min", DEFAULT_MIN))
            max_first = int(request.args.get("maxFirst", max_val))
            min_first = int(request.args.get("minFirst", min_val))

            expression = generator.division(max_first, min_first)
            return jsonify(expression)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def random_operation():
        try:
            max_val = int(request.args.get("max", DEFAULT_MAX))
            min_val = int(request.args.get("min", DEFAULT_MIN))
            max_first = int(request.args.get("maxFirst", max_val))
            min_first = int(request.args.get("minFirst", min_val))
            max_second = int(request.args.get("maxSecond", max_val))
            min_second = int(request.args.get("minSecond", min_val))
            negative = bool(int(request.args.get("negative", 0)))

            expression = generator.random_operation(max_first, min_first, max_second, min_second, negative)
            return jsonify(expression)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def root_redirect():
        """
        Returns a funny math number with a witty comment.
        """
        funny_numbers = [
            {"number": 3.14159, "description": "Pi - Deliciously infinite!"},
            {"number": 2.71828, "description": "e - Naturally exponential!"},
            {"number": 1.61803, "description": "Golden Ratio - Fibonacci-approved!"},
            {"number": "∞", "description": "Infinity - Can't count this one."},
            {"number": "-0", "description": "Negative zero? Mind blown."},
            {"number": "5i", "description": "Imaginary number - It's not real, but it works!"},
            {"number": "undefined", "description": "Divided by zero. Oops!"},
            {"number": 42, "description": "42 - The Answer to the Ultimate Question of Life."},
            {"number": 69, "description": "Nice."},
            {"number": 404, "description": "Not Found... Just kidding, it's math!"}
        ]

        # Choose a random funny number
        funny_number = random.choice(funny_numbers)
        return jsonify(funny_number)
