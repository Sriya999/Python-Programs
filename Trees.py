class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
        
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def print_tree(self):
        #print by spaces
        spaces='  '*self.get_level()*2
        prefix=spaces+"|--" if self.parent else ""
        #leaf node
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    def get_level(self):
        p=self.parent
        level=0
        while p:
            level+=1
            p=p.parent
        return level
            
def BuildTree():
    #root element of tree
    
    root=TreeNode("Electronice")
    laptop=TreeNode("laptop")
    root.add_child(laptop)
    tv=TreeNode("TV")
    root.add_child(tv)
    
    hp=TreeNode("hp")
    dell=TreeNode("dell")
    laptop.add_child(hp)
    laptop.add_child(dell)
    sony=TreeNode("sonytv")
    tv.add_child(sony)
    
    return root
root=BuildTree()
root.print_tree()

print(root.get_level())

    
