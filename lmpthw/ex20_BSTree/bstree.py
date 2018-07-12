class BSNode(object):
    """ Creates a BS node """

    def __init__(self, key, value, left, right, parent):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BSTree(object):

    def __init__(self, key, left, right):

        self.key = key
        self.left = left
        self.right = right

   def get(self, key):

       node = BSNode()

       # if no left or right child:
           return None

       # You go left if the given key is less-than the node's key. 
       elif key < node.key:
           # go left
           node = node.left
           if key == node.left:
               return node.value
       # You go right if the key is greater-than the node's key.
       elif key > node.key:
           # go right
           node = node.right
           if key == node.right:
               return node.value
       # There is a way to do this using recursion and using a while loop.

    def set(self, key, value):
       # Given a key, walk the tree to find the node, 
       # or return None if you reach a dead end. 
       # You go left if the given key is less-than the node's key. 
       # You go right if the key is greater-than the node's key. 
       # If you read a node with no left or right, you attach a new node 
       # on the left or right, thus extending the tree down one more branch.

    def delete(self):

        # you have three conditions: 
        # If it's a leaf then just remove it. 
        # If it has one child, then replace it with the child. 
        # If it has two children, then it gets really complicated 

    def list(self):

        # Walk the tree and print everything out. 
        # The important piece to list is that you can walk the tree in different ways to produce different output. 
        # If you walk the left, then the right paths, you get something different than if you do the inverse. 
        # If you go all the way to the bottom and then print as you come up the tree toward root, you get yet another kind of output. 
        # You can also print the nodes as you go down the tree, from root to the "leaves".


