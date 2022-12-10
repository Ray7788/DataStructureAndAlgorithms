import config

class bstree:
    def __init__(self):
        self.verbose = config.verbose
        self.left = None
        self.right = None
        self.value = ""
        self.heights = 0
        self.count_search = 0
        
    def size(self):
        if self.value is not None:
            # Check if the left node and right node are none and calculate the sum
            if (self.left is not None) and (self.right is not None):
                return 1 + self.left.size() + self.right.size()
            elif (self.left is not None) and (self.right is None):
                return 1 + self.left.size()
            elif (self.left is None) and (self.right is not None):
                return 1 + self.right.size()
            elif (self.left is None) and (self.right is None):
                return 1
        else:
            pass
        
    def tree(self):
        # This counts as a tree if it has a field self.value, it also include sub-trees self.left and self.right
        return hasattr(self, 'value') and hasattr(self, 'left') and hasattr(self, 'right')
        
    def insert(self, value):
        if self.tree():
            # If the root node is None, then insert the value here
            # if tree is not NULL then insert into the correct sub-tree
            if self.value == value:
                return
            # If parent node's value is larger than the target value
            elif self.value > value:
                if self.left == None:
                    self.left = bstree()
                    self.left.value = value
                    return
                else:
                    self.left.insert(value)
            # If parent node's value is smaller than the target value
            elif self.value < value:
                if self.right is None:
                    self.right = bstree()
                    self.right.value = value
                    return 
                else:
                    self.right.insert(value)
        else:
            # otherwise create a new node containing the value
            self.value = value
            self.left = None
            self.right = None
        
    def find(self, value):
        if self.tree():
            # find the corrct value at once
            if self.value == value:
                return True
            # the value is smaller than the index value
            if self.value > value:
                if self.left is None:
                    return False
                else:
                    return self.left.find(value)
            # the value is larger than than the index value
            if self.value < value:
                if self.right is None:
                    return False
                else:
                    return self.right.find(value)
        else:
            # if the root node is None, return False 
            return False
        
    # You can update this if you want
    def print_set_recursive(self, depth):
        if (self.tree()):
            for i in range(depth):
                print(" ", end='')
            print("%s" % self.value)
            #  print left hand side
            if self.left is not None:
                self.left.print_set_recursive(depth + 1)
            else:
                for i in range(depth):
                    print(" ", end='')
                print("%s" % "lEFT_NODE")
            # print right hand side
            if self.right is not None:
                self.right.print_set_recursive(depth + 1)
            else:
                for i in range(depth):
                    print(" ", end='')
                print("%s" % "RIGHT_NODE")
    
    # calculate heights
    def height(self):
        if(self.left != None):
            left_size = self.left.height()
        else:
            left_size = 0

        if(self.right != None):
            right_size = self.right.height()
        else:
            right_size = 0

        return 1 + max(left_size, right_size) 
            
    # You can update this if you want
    def print_set(self):
        print("Tree:\n")
        self.print_set_recursive(0)
        
    def print_stats(self):
        self.heights = self.height()
        if self.verbose == 0:
            return
        elif self.verbose == 1:
            print("Tree height is: ", self.heights)
        elif self.verbose == 2:
            print("Tree height is: ", self.heights)
            print("Amount of searches for insert: ", self.count_search)
        elif self.verbose == 3:
            print("Tree height is: ", self.heights)
            print("Amount of searches for insert: ", self.count_search)
            print("Tree size: ", self.size())