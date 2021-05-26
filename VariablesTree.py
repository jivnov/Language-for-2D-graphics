import treelib

class VariablesTree:

    def __init__(self):
        self.tree = treelib.Tree()
        self.tree.create_node(tag="GlobalVars", identifier="GlobalVars")

    def add_variable(self, tag, name, content, scope=None):
        '''

        :param name: name of the variable added
        :param content: Vertex or Graph representing the variable
        :param scope: name of the function the variable is being created in or None in case it's a global variable

        '''
        if scope is None:
            self.tree.create_node(tag=tag, identifier=name, parent=self.tree.get_node(nid="GlobalVars"), data=content)
            self.tree.show()
            return
        self.tree.create_node(tag=tag, identifier=name, parent=self.tree.get_node(nid=scope), data=content)
        self.tree.show()

    def add_scope_subtree(self, tag,  name, scope=None):
        '''

        :param name: name of the variable added
        :param scope: name of the function the variable is being created in or None in case it's a global variable

        '''
        if scope is None:
            self.tree.create_node(tag=tag, identifier=name, parent=self.tree.get_node(nid="GlobalVars"))
            self.tree.show()
            return
        self.tree.create_node(tag=tag, identifier=name, parent=self.tree.get_node(nid=scope))

        self.tree.show()

