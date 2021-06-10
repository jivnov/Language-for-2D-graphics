import treelib
from exceptions import VariableNotFoundError

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
            return
        self.tree.create_node(tag=tag, identifier=name, parent=self.tree.get_node(nid=scope), data=content)

    def add_scope_subtree(self, tag, name, scope=None):
        '''

        :param name: name of the variable added
        :param scope: name of the function the variable is being created in or None in case it's a global variable

        '''
        if scope is None:
            self.tree.create_node(tag=tag, identifier=name, parent=self.tree.get_node(nid="GlobalVars"))
            return
        self.tree.create_node(tag=tag, identifier=name, parent=self.tree.get_node(nid=scope))


    def find_var_by_tag(self, tag, scope=None):
        '''

        :param tag: tag(name) of the variable
        :param scope: the most inner scope to look in (nid)
        :return: data from a node of the variable tree or raise exception

        '''

        if scope is None:
            scope = self.tree.root

        scope_vars = self.tree.children(scope)

        vars_found = list(filter(lambda x: x.tag == tag, scope_vars))

        while len(vars_found) == 0 and self.tree.parent(scope) is not None:
            scope = self.tree.parent(scope).identifier
            scope_vars = self.tree.children(scope)

            vars_found = list(filter(lambda x: x.tag == tag, scope_vars))

        if len(vars_found) == 0:
            raise VariableNotFoundError(tag)

        return vars_found[0]
