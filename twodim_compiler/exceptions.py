"""
===============================================================================
================================= GRAPH ERRORS ================================
===============================================================================
"""

class DisconnectedGraphException(Exception):
    pass


class UndeclaredShapeException(Exception):
    pass


class UndefinedShapeException(Exception):
    pass


class RedundantRelationException(Exception):
    pass


class UndefinedRelationException(Exception):
    pass


class RedefiningExplicitRelationException(Exception):
    pass


class CyclicRelationsException(Exception):
    pass

"""
===============================================================================
============================ VARIABLES TREE ERRORS ============================
===============================================================================
"""

class VariableNotFoundError(Exception):
    pass

"""
===============================================================================
=============================== FUNCTION ERRORS ===============================
===============================================================================
"""

class FunctionSignatureError(Exception):

    def __init__(self, function_name):
        self.function_name = function_name

    def __str__(self):
        return f"Function {self.function_name}() signature does not match the declaration. " \
               f"Check if arguments in the call correspond to declaration."


class FunctionNotExistsError(Exception):

    def __init__(self, function_name):
        self.function_name = function_name
        self.message = f"Function {self.function_name}() is not defined."

    def __str__(self):
        return self.message


class MultipleDeclarationsError(Exception):

    def __init__(self, function_name):
        self.function_name = function_name
        self.message = f"Function {self.function_name}() is declared multiple times."

    def __str__(self):
        return self.message

