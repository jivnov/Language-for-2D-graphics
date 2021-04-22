import sys
import drawSvg as d
from graph import Shape, Vertex

class Drawing2d:
    def __init__(self, w, h):
        self.viewport_width = w 
        self.viewport_height = h
        self.canvas = d.Drawing(w, h, origin="center")

    def draw(self, v: Vertex):
        if (v.shape == Shape.RECT):
            x = -1 * v.bb_w * self.viewport_width /2
            y = -1 * v.bb_h * self.viewport_height /2
            r = d.Rectangle(x, y, v.bb_w*self.viewport_width, v.bb_h * self.viewport_height)
            self.canvas.append(r)

            

    
