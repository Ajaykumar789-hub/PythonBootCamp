class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def print_bt_detaild(root):
    if root == None:
        return
    print(root.data, end= ": ")
    if root.left:
        print(f"L-->{root.left.data}", end=",")
    else:
        print("L-->None", end=",")
    
    if root.right:
        print(f"R-->{root.right.data}", end=",")
    else:
        print("R-->None", end=",")

    print_bt_detaild(root.left)
    print_bt_detaild(root.right)
def take_input_bt():
    data = int(input("Enter the data for the Node: "))
    if data == -1:
        return
    node = BinaryTreeNode(data)
    print(f"Enter the left child of {data}: ")
    node.left = take_input_bt()
    print(f"Enter the right child of {data}: ")
    node.right = take_input_bt()

    return node

# root = take_input_bt()
# print_bt_detaild(root)

from collections import deque
def take_input_bt_level_wise():
    data = int(input(f"Enter the data for root: "))
    if data == -1:
        return
    root = BinaryTreeNode(data)
    queue = deque([root])
    while len(queue) != 0:
        current_node = queue.popleft()
        left_child_data = int(input(f"Enter left child for {current_node.data}: "))
        if left_child_data != -1:
            left_node = BinaryTreeNode(left_child_data)
            current_node.left = left_child_data
            queue.append(left_node)

        right_child_data = int(input(f"Enter right child for {current_node.data}: "))
        if right_child_data != -1:
            right_node = BinaryTreeNode(right_child_data)
            current_node.right = right_child_data
            queue.append(right_node)
    
    return root

root = take_input_bt_level_wise()
print_bt_detaild(root)

