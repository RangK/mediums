# 1. Help
class ParentA:
    def __int__(self):
        self._name = "ParentA"

class Child(ParentA):
    def __int__(self):
        self._name = "Child"

help(Child)
"""
class Child(ParentA)
 |  Method resolution order:
 |      Child
 |      ParentA
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __int__(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from ParentA:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

"""