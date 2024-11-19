from genericTressInput import predefined_generic_tree_inputs
from collections import deque

root1, root2, root3 = predefined_generic_tree_inputs()

def largest_values_in_tree(root):
    if root == None:
        return []
    result = []
    queue = deque([queue])
    while queue:
        n = len(queue)
        max_val = float('-inf')
        for _ in range(n):
            node = queue.popleft()
            max_val = max(max_val, node.val)
            for child in node.children:
                queue.append(child)
        result.append(max_val)
    return result
print(largest_values_in_tree(root1))