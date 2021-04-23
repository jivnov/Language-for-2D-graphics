import sys
import svgwrite as d
from graph import Shape, Vertex

filename = "example.svg"

class Drawing2d:
    def __init__(self, w, h):
        self.viewport_width = w 
        self.viewport_height = h
        self.canvas = d.Drawing(filename, (w, h))

    def draw(self, v: Vertex):
        if (v.shape == Shape.RECT):
            x = self.viewport_width/2 * (1 - v.bb_w)
            y = (1 - v.bb_h) * self.viewport_height /2
            r = self.canvas.rect((x, y), (v.bb_w*self.viewport_width, v.bb_h * self.viewport_height))
            self.canvas.add(r)


            

    
