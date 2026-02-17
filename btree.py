

class BinaryNode:
    def __init__(self, entry):
        self._right = None
        self._left = None
        self._entry = entry
    def is_leaf(self):
        if self._right== None and self._left == None: return True
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
        self.deepest = 0
    def add(self, entry) -> None:
        """Adds to binary tree, allows skewed"""
        userEntryNode = BinaryNode(entry)
        if self._adam == None:
            self._adam = userEntryNode
            return None
        else: 
            #okay now we have to check the value of the node accessed
            #maybe you guys want me to do this recursively but i don't
            #like (n * n!) O time (especially in Python) so we're looping
            currentBNode = self._adam
            previousBNode = None
            deepestInFunction = 0
            #while the currentBNode is actually a BNode
            while hasattr(currentBNode, "_entry"):
                if deepestInFunction == self.deepest+1:
                    self.deepest += 1 #increase deepest amount
                #previous was the former current
                previousBNode = currentBNode
                #decide what direction we go into based on the size
                #we're using integers for the first lab so this works
                if currentBNode.get_entry() > userEntryNode.get_entry():
                    #right leaning >
                    print("chose right")
                    currentBNode = currentBNode.get_branch("right")
                elif currentBNode.get_entry() < userEntryNode.get_entry():
                    print("chose left")
                    currentBNode = currentBNode.get_branch("left") #lower value so left >
                elif currentBNode.get_entry() == userEntryNode.get_entry():
                    raise Exception("Duplicates not allowed as per the rule of Rex Noster Gibbons. Long live the king!!!")

                deepestInFunction += 1 #we've finished one layer so far
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
            print(self.deepest)
            return None
    def getAllNodesInTree(self, startNode: BinaryNode, binaryNodeList: list, levelBNL: int) -> list:
        print(f"I'm at level {levelBNL}")
        if startNode == None:
            return [] #there's no left or right side return empty list
        binaryNodeList[levelBNL].append(startNode)
        if not startNode.is_leaf():
            if startNode.has_branch("left"):
                binaryNodeList = self.getAllNodesInTree(startNode.get_branch("left"), binaryNodeList, levelBNL+1)
            if startNode.has_branch("right"):
                binaryNodeList = self.getAllNodesInTree(startNode.get_branch("right"), binaryNodeList, levelBNL+1)
        return binaryNodeList
    def display(self, sortMethod):
        """Displays the node by returning a string in the method they want"""
        #make an empty list the depth length with lists in them
        leftDepth = [[] for _ in range(self.deepest+1)]
        rightDepth = [[] for _ in range(self.deepest+1)]
        leftList = self.getAllNodesInTree(self._adam.get_branch("left"), leftDepth, 0)
        rightList = self.getAllNodesInTree(self._adam.get_branch("right"), rightDepth, 0)
        center = self._adam
        listOfLeftNodes = [a for a in leftList]
        print(listOfLeftNodes)
        listOfRightNodes = [a for a in rightList]
        match sortMethod:
            case self.preOrder:
                print("Center: " + self._adam.get_entry())
                print("Left Nodes:", end="")
                for leftLevelArray in listOfLeftNodes:
                    for leftLANode in leftLevelArray:
                        print("(" + str(leftLANode.get_entry()) + ")", end="")
                print("\nRight Nodes:", end="")
                for rightLevelArray in listOfRightNodes:
                    for rightLANode in rightLevelArray:
                        print("(" + str(rightLANode.get_entry()) + ")", end="")
            case self.inOrder:
                print("Left Nodes:", end="")                
                for leftLevelArray in listOfLeftNodes:
                    for leftLANode in leftLevelArray:
                        print("(" + str(leftLANode.get_entry()) + ")", end="")
                print("Center: " + self._adam.get_entry())                
                print("\nRight Nodes:", end="")             
                for rightLevelArray in listOfRightNodes:
                    for rightLANode in rightLevelArray:
                        print("(" + str(rightLANode.get_entry()) + ")", end="")
