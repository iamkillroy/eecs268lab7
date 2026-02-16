

class BinaryNode:
    def __init__(self, entry):
        self._right = None
        self._left = None
        self._entry = entry
    def is_leaf(self):
        if self.right == None and self.left == None: return True
        else: return False
    def get_entry(self):
        return self._entry
    def get_branch(self, branchDirection: str):
        if branchDirection == "left":
            return self._left
        elif branchDirection == "right":
            return self._right
        else:
            raise Exception("Cannot get nonexistant branch {branchDirection}")
    def set_branch(self, branchDirection: str, node):
        if branchDirection == "left":
            self._left = node
        elif branchDirection == "right":
            self._right = node
        else:
            raise Exception(f"Branch direction \"{branchDirection}\" doesn't exist")

class BinaryTree:
    def __init__(self):
        self._adam = None
    def add(self, entry) -> None:
        """Adds to binary tree, allows skewed"""
        userEntryNode = BinaryNode(entry)
        if self._adam == None:
            print("set ada")
            self._adam = userEntryNode
            return None
        else: 
            #okay now we have to check the value of the node accessed
            #maybe you guys want me to do this recursively but i don't
            #like (n * n!) O time (especially in Python) so we're looping
            currentBNode = self._adam
            previousBNode = None
            #while the currentBNode is actually a BNode
            while hasattr(currentBNode, "_entry"):
                #previous was the former current
                previousBNode = currentBNode
                #decide what direction we go into based on the size
                #we're using integers for the first lab so this works
                if currentBNode.get_entry() >= userEntryNode.get_entry():
                    #right leaning >=
                    currentBNode = currentBNode.get_branch("right")
                else:
                    currentBNode = currentBNode.get_branch("left") #lower value so left >
            #we've broken out of the loop!!!
            #now we know that the result of the currentNode is undefined
            #so we wanna go back and see what branch (left, right) we should 
            #put the previous node                |------> None (currentNode maybe)
            # so we're here --->      previousNode|
            #                                     |-------> None (currentNode maybe)
            if previousBNode.get_entry() >= userEntryNode.get_entry(): #if it's right go right
                previousBNode.set_branch("right", userEntryNode)
            else: #if it's left go left
                previousBNode.set_branch("left", userEntryNode)
            return None
