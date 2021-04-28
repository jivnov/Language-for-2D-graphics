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
        self.canvas = svg.Drawing('generated_images/output.svg', (w, h))

    def draw(self, v: Vertex):
        # TODO: Draw all neighbours and neighbours' neighbours etc.
        """
        Basic algo:
        1. Go "up" (check the IN reference) until you reach the root of the graph
        NOTE: When adding a neighbour A to a Vertex B CONTAINED in some shape X, you should add "A IN X" relation automatically as well
        2. Draw root shape X
        3. Call algo for each of X's neighbours until there are no neighbours to draw
        :param v:
        :return:
        """
        draw_shape = None
        if (v.shape == Shape.RECT):
            x = (1 - v.bb_w) * self.viewport_width / 2
            y = (1 - v.bb_h) * self.viewport_height / 2
            draw_shape = self.canvas.rect(insert=(x, y),
                                          size=(v.bb_w * self.viewport_width, v.bb_h * self.viewport_height))
        if (v.shape == Shape.SQUARE):
            x = (1 - v.bb_w) * self.viewport_width / 2
            y = self.viewport_height / 2 - (v.bb_h * self.viewport_width / 2)
            draw_shape = self.canvas.rect(insert=(x, y),
                                          size=(v.bb_w * self.viewport_width, v.bb_h * self.viewport_width))
        if (v.shape == Shape.CIRCLE):
            x = self.viewport_width / 2
            y = self.viewport_height / 2
            draw_shape = self.canvas.circle(center=(x, y), r=(v.bb_w * self.viewport_width / 2))
        self.canvas.add(draw_shape)

    def _graph_to_something_insertable(self, graph: Graph):
        # TODO: This helper method should enable defining relations between Vertices and Graphs
        # TIP: We may want to use <defs> tag for this
        pass