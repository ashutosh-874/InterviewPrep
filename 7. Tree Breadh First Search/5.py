class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque
def find_minimum_depth(root):
    if root is None:
        return 0
    q = deque()
    q.append(root)
    minDepth = 0

    while q:
        qLen = len(q)
        minDepth += 1
        for _ in range(qLen):
            node = q.popleft()
            
            if not node.left and not node.right:
                return minDepth
            
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)





def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
