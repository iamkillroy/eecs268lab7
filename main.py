from btree import BinaryNode, BinaryTree

bt = BinaryTree()

while __name__ == "__main__":
    userOption = input("""Lucas' Binary Tree Lab 7\n\t(1) - Add values\n\t(2) - Print Binary Tree\n\t(3) - Quit""")
    if userOption == "1":
        userList = input("Put your input in a comma seperated list. \nWhen does, type enter. Don't include ] to end the list\n").split(",")
        for userInteger in userList:
            bt.add(int(userInteger.replace(",", "")))
    if userOption == "2":
        method = input("What method do you want to display (pre, in, post)")
        if bt._adam != None:
            bt.display(method)
    if userOption == "3":
        break


