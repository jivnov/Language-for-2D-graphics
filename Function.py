
from typing import List
from graph import Shape

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

