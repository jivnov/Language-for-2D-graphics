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
        self.canvas = d.Drawing(filename, (w, h))

    def draw(self, v: Vertex):
        draw_shape = None
        if (v.shape == Shape.RECT):
            x = (1 - v.bb_w) * self.viewport_width / 2
            y = (1 - v.bb_h) * self.viewport_height /2    
            draw_shape = self.canvas.rect(insert = (x, y), size = (v.bb_w*self.viewport_width, v.bb_h * self.viewport_height))
        if (v.shape == Shape.SQUARE):
            x = (1 - v.bb_w) * self.viewport_width / 2
            y = self.viewport_height /2 - (v.bb_h * self.viewport_width /2) 
            draw_shape = self.canvas.rect(insert = (x, y), size = (v.bb_w*self.viewport_width, v.bb_h * self.viewport_width))
        if (v.shape == Shape.CIRCLE):
            x = self.viewport_width / 2
            y = self.viewport_height / 2
            draw_shape = self.canvas.circle(center = (x, y), r = (v.bb_w * self.viewport_width / 2))
        self.canvas.add(draw_shape)


            

    
