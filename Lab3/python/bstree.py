import config

class bstree:
    def __init__(self):
        self.verbose = config.verbose
        self.left = None
        self.right = None
        self.height = 0
        
    def size(self):
        if (self.tree()):
            return 1 + self.left.size() + self.right.size()
        return 0
        
    def tree(self):
        # This counts as a tree if it has a field self.value
        # it should also have sub-trees self.left and self.right
        # return hasattr(self, 'value')
        if hasattr(self, 'value') and hasattr(self, 'left') and hasattr(self, 'right'):
            return self.value != None and self.left != None and self.right != None
        
    def insert(self, value):
        # if tree is not NULL then insert into the correct sub-tree
        if (self.tree()):
            if self.value == value:
                return
            # If parent node's value is larger than the target value
            elif self.value > value:
                if self.left is None:
                    self.left = bstree(value)
                else:
                    self.left.insert(value)
            # If parent node's value is smaller than the target value
            elif self.value < value:
                if self.right is None:
                    self.right = bstree(value)
                else:
                    self.right.insert(value)
        else:
            # otherwise create a new node containing the value
            self.value = value
        
    def find(self, value):
        if self.tree():
            # find the corrct value at once
            if self.value == value:
                return True
            # the value is smaller than the index value
            if value < self.value:
                if self.left != None:
                    return self.left.find(value)
                else:
                    return False
            # the value is larger than than the index value
            elif value > self.value :
                if self.right != None:
                    return self.right.find(value)
                else:
                    return False
        # if the root node is None, return False 
        else:
            if self.value is None:
                return False
        
    # You can update this if you want
    def print_set_recursive(self, depth):
        if depth == 0:
            self.height = depth
        if (self.tree()):
            for i in range(depth):
                print(" ", end='')
            print("%s" % self.value)

            # left hand side
            if self.left is not None:
                self.height = max(self.height, depth + 1)
                self.left.print_set_recursive(depth + 1)
            else:
                for i in range(depth):
                    print(" ", end='')
                print("%s" % "lEFT_NODE")

            #  right hand side
            if self.right is not None:
                self.height = max(self.height, depth + 1)
                self.right.print_set_recursive(depth + 1)
            else:
                for i in range(depth):
                    print(" ", end='')
                print("%s" % "RIGHT_NODE")
            
    # You can update this if you want
    def print_set(self):
        print("Tree:\n")
        self.print_set_recursive(0)
        
    def print_stats(self):
        # record and print statistic
        print("Size of the tree : " + str (self.size()))
        print("Height of the tree : " + str (self.height()))
            
            