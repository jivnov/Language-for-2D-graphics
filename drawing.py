import sys
import drawSvg as d

class Drawing2d:
    def __init__(self, w, h):
        self.viewport_width = w 
        self.viewport_height = h
        self.canvas = d.Drawing(w, h, origin="center")

    
