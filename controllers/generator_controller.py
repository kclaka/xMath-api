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
