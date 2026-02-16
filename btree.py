

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
    def has_branch(self, branchDirection: str):
        if branchDirection == "left" and self._left != None:
            return True
        if branchDirection == "right" and self._right != None:
            return True
        return False #else
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
        self.preOrder = "pre"
        self.inOrder = "in"
        self.postOrder = "post"
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
                if currentBNode.get_entry() > userEntryNode.get_entry():
                    #right leaning >
                    currentBNode = currentBNode.get_branch("right")
                elif currentBNode.get_entry() < userEntryNode.get_entry():
                    currentBNode = currentBNode.get_branch("left") #lower value so left >
                elif currentBNode.get_entry() == userEntryNode.get_entry():
                    raise Exception("Duplicates not allowed as per the rule of Rex Noster Gibbons. Long live the king!!!")
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
    def display(self, method):
        """Displays the node by returning a string in the method they want"""
        ###okay this is gonna get hard
        #we gotta traverse the tree to start with at the left most nth element up till the parent
        leftMostBNode = self._adam
        rightMostBNode = self._adam
        allLeftNodes = []
        allRightNodes = []
        #traverse the binary tree until the leftmost node tree occurs
        #this happens by checking if there's a new node in the left branch
        #and if not, just deferring left every time
        while hasattr(self._adam.get_branch("left"), "_left"):
            allLeftNodes.append(leftMostNode)
            leftMostBNode = leftMostBNode.get_branch("left")
        #we're going to do the same thing for the right now
        while hasattr(self._adam.get_branch("right", "_right")):
            allRightNodes.append(rightMostNode)
            rightMostBNode = rightMostBNode.get_branch("right")
        #okay so now we have all leftmost nodes in a list
        #and all rightmost nodes in a list and the best way that we
        #can display them is by traversing them and displaying them in a string
        levelStringListLeft = []
        levelStringListRight = []
        #okay now we gotta flip the lists over so we can start with the bottom and go 
        #up to the top
        allLeftNodes.reverse()
        allRightNodes.reverse()
        #so the level string represents where we are at the level
        #starts at 0 and goes up to n levels to the adam of the binary tree
        #when we find the leftmost node value has a right node,
        #we go down levelInt-1. assume that the right node also has a left
        #node that we didn't catch (allLeftNodes are only leftmostnodes) then
        #we go down another level up until there's nothing, and then come back up
        for levelInt, leftNodeAtLayer in enumerate(allLeftNodes):
            #the current levelString is equal to the leftnode at layer
            #remember for each level of recursion this would be the tallest layer
            #we can only go down from here so it's okay to just say this is the top
            levelStringListLeft[levelInt] = "("+leftNodeAtLayer.get_entry()+")"
            if not leftNodeAtLayer.is_leaf(): 
                #check to see if there's no child nodes to display
                #if this is true then there's either a left or right
                #bnode to display
                moreBranchesToFind = False
                leftNodeDeeper = leftNodeAtLayer
                while not moreBranchesToFind:
                    bottomBranchEntry = ""
                    layerDownLevelInt = levelInt - 1 #let's go one layer down
                    if leftNodeDeeper.has_branch("left"):
                        bottomBranchEntry = bottomBranchEntry + "(" +leftNodeAtLayer.get_branch("left").get_entry() + ")"
                    if leftNodeDeeper.has_branch("right"):
                        bottomBranchEntry = bottomBranchEntry + "(" + leftNodeAtLayer.get_branch("right").get_entry() + ")"
                    #now that we've added all of the branches at this level let's see
                    #if there's a further level for us to scan
                    if not leftNodeDeeper.get_branch("right").is_leaf() or not leftNodeDeeper.get_branch("left").is_leaf():
                        #this means that the ends of those nodes aren't actually the ends. we go deeper to each of them
                        pass
        if method == self.pre:
            pass
