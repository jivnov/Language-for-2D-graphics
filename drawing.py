import sys
import svgwrite as svg
from graph import Shape, Vertex, Relation, Graph

import random


class Drawing2d:
    def __init__(self, w, h):
        """
        :param w:
        :param h:
        """
        self.viewport_width = w
        self.viewport_height = h
        self.canvas = svg.Drawing('generated_images/output.svg', (w, h))

    def draw(self, v: Vertex, parent: Vertex = None):
        # TODO: Draw all neighbours and neighbours' neighbours etc.
        """
        Basic algo:
        1. Go "up" (check the IN reference) until you reach the root of the graph
        NOTE: When adding a neighbour A to a Vertex B CONTAINED in some shape X, you should add "A IN X" relation automatically as well
        2. Draw root shape parent_graphX
        3. Call algo for each of X's neighbours until there are no neighbours to draw
        :param parent: Parent of the vertex; if None, assume this is the root
        :param v:
        :return:
        """
        if v.drawn:
            return
        # if parent is None and v.IN is None:
        #     # Determine drawing position using viewport only
        #     v.x = (1 - v.bb_w) * self.viewport_width / 2
        #     v.y = (1 - v.bb_h) * self.viewport_height / 2
        #
        #     # Determine drawing size (in px) using viewport dimensions only
        #     v.width = v.bb_w * self.viewport_width
        #     v.height = v.bb_h * self.viewport_height
        draw_shape = None
        draw_color = tuple(random.randint(0, 256) for _ in range(3))
        if v.shape == Shape.RECT:
            draw_shape = self.canvas.rect(insert=(v.x, v.y),
                                          size=(v.width, v.height), fill="rgb" + str(draw_color))
        if v.shape == Shape.SQUARE:
            x = (1 - v.bb_w) * self.viewport_width / 2
            y = self.viewport_height / 2 - (v.bb_h * self.viewport_width / 2)
            draw_shape = self.canvas.rect(insert=(v.x, v.y),
                                          size=(v.bb_w * self.viewport_width, v.bb_h * self.viewport_width))
        if v.shape == Shape.CIRCLE:
            x = self.viewport_width / 2
            y = self.viewport_height / 2
            draw_shape = self.canvas.circle(center=(v.x, v.y), r=(v.bb_w * self.viewport_width / 2))
        self.canvas.add(draw_shape)
        v.drawn = True

        for peer in v.LEFT | v.RIGHT | v.TOP | v.BOT:
            self.draw(peer, v)

    def _graph_to_something_insertable(self, graph: Graph):
        # TODO: This helper method should enable defining relations between Vertices and Graphs
        # TIP: We may want to use <defs> tag for this
        pass
