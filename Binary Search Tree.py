class BST:
    def __init__(self,key):
            self.key=key
            self.lchild=None
            self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        # Ignoring duplicate data 
        if self.key==data:
            return
        
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)

        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
                
    def delete(self,data): 
    
        if self.key is None:
            print("Tree is empty")
            return
        
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("Given node is not present in the tree")
                
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("Given node is not present in the tree")
                    
        else:
            #If node contains 0 child
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            #If node contains 1 child
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self
            
            

    def search(self,data):
            if self.key is None:
                print("Node is not present in the tree!")
                return

            if self.key==data:
                print("Node is present")
                return

            if self.key>data:
                if self.key is None:
                    print("Node is not present in the tree!")
                    return

                if self.lchild:
                    self.lchild.search(data)
                else:
                    print("Node is not present in the tree!")

            else:
                if self.rchild:
                    self.rchild.search(data)
                else:
                    print("Node is not present in the tree!") 

    def preorder(self):
            if self.key is None:
                return 
            print(self.key,end=" ")
            if self.lchild:
                self.lchild.preorder()
            if self.rchild:
                self.rchild.preorder()

    def inorder(self):
            if self.key is None:
                return 
            if self.lchild:
                self.lchild.inorder()
            print(self.key,end=" ")
            if self.rchild:
                self.rchild.inorder()

    def postorder(self):
            if self.key is None:
                return 
            if self.lchild:
                self.lchild.postorder()
            if self.rchild:
                self.rchild.postorder()
            print(self.key,end=" ")
            
    

root=BST(5)
list1=[2,6,845,4,56,42,24,65,87,65,78]
for i in list1:
    root.insert(i)
print("Pre-order traversal:",end=" ")
root.preorder()
print()
print("In-order traversal:",end=" ")
root.inorder()
print()
print("Post-order traversal:",end=" ")
root.postorder()
print()
print(root.height())
