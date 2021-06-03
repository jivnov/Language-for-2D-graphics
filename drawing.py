import sys
import svgwrite as svg
from graph import Shape, Vertex, Relation, Graph

import random


class Drawing2d:
    def __init__(self, w, h, output_path='generated_images/output.svg'):
        """
        :param w:
        :param h:
        """
        self.viewport_width = w
        self.viewport_height = h
        self.canvas = svg.Drawing(output_path, (w, h))

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

        v.draw(self.canvas)

    def _graph_to_something_insertable(self, graph: Graph):
        # TODO: This helper method should enable defining relations between Vertices and Graphs
        # TIP: We may want to use <defs> tag for this
        pass
