class SplayNode:
    def __init__(self,value,left,right,parent):
        self.value=value
        self.left=left
        self.right=right
        self.parent=parent

class Splay:
    def __init__(self,root):
        self.root=root

    def splay(self,node):
        if not node.parent.parent:
            self.zig(node)

    def zig(self,node):
