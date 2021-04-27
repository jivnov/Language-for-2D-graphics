import sys
import svgwrite as svg
from graph import Shape, Vertex


class Drawing2d:
    def __init__(self, w, h):
        """

        :param w:
        :param h:
        """
        self.viewport_width = w
        self.viewport_height = h
        self.canvas = svg.Drawing(size=(w, h), filename='generated_images/svgwrite_example.svg')

    def draw(self, v: Vertex):
        if v.shape == Shape.RECT:
            x = -1 * v.bb_w * self.viewport_width / 2
            y = -1 * v.bb_h * self.viewport_height / 2
            self.canvas.add(self.canvas.rect(insert=(x, y), size=(v.bb_w * self.viewport_width, v.bb_h * self.viewport_height)))
