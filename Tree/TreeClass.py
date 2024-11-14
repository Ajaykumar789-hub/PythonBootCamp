class TreeNode:
    def __init__(self,data):
        self.data = data
        self.childern = []

root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

root.childern.append(child1)
root.childern.append(child2)
root.childern.append(child3)

print(root.childern[0].data)


