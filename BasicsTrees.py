class TreeNode:
    def __init__(self,data,designation):
        self.data=data
        self.children=[]
        self.designation=designation
        self.parent=None
        
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
        
        
    def print_tree(self,property):
        if property=='both':
            value=self.data+"("+self.designation+")"
        elif property=='data':
            value=self.data
        else:
            value=self.designation
        #spaces
        spaces=" "*self.get_level()*3
        #prefix
        prefix=spaces+"|__" if self.parent else ""
        #calls
        print(prefix+value)
        if self.children:
            for child in self.children:
                child.print_tree(property)
    def get_level(self):
        p=self.parent
        level=0
        while p:
            level+=1
            p=p.parent
        return level
            
def BuildTree():
    #root element of tree
    
    root=TreeNode("sriya","CEO")
    laptop=TreeNode("pri","manager")
    root.add_child(laptop)
    tv=TreeNode("sita","head")
    root.add_child(tv)
    
    hp=TreeNode("gita","asst manager")
    dell=TreeNode("sri","junior dev")
    laptop.add_child(hp)
    laptop.add_child(dell)
    
    return root
root=BuildTree()

print(root.get_level())
root.print_tree('both')
    
