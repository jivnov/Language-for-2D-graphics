from graph import Shape
from typing import List

class FunctionSignatureError(Exception):

    def __init__(self, function_name):
        self.function_name = function_name

    def __str__(self):
        return f"Function {self.function_name}() signature does not match the declaration."


class FunctionNotExistsError(Exception):

    def __init__(self, function_name):
        self.function_name = function_name

    def __str__(self):
        return f"Function {self.function_name}() is not defined."


class Function:
    def __init__(self, name: str, args: List, args_names: List = None, body=None):
        # expecting to receive list of pairs [Shape, Int] where Int is a counter for provided shape
        self.name = name
        self.args = []
        self.args_names = args_names

        for shape, count in args:
            if shape == "rect":
                shape = Shape.RECT
            elif shape == "square":
                shape = Shape.SQUARE
            elif shape == "circle":
                shape = Shape.CIRCLE
            elif shape == "triangle":
                shape = Shape.TRIANGLE
            elif shape == "shape":
                shape = Shape.SHAPE
            self.args.append((shape, count))

        self.body = body

