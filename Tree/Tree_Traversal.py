from genericTressInput import predefined_generic_tree_inputs
from collections import deque

root1, root2, root3 = predefined_generic_tree_inputs()

def tree_Traversal(root):
    if root == None:
        return []
    result = []
    queue = deque([root])
    while queue:
        n = len(queue)
        level_nodes = []        
        for _ in range(n):
            node = queue.popleft()
            level_nodes.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)

    return result