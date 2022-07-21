from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):

    result = []
    q = deque()
    q.append(root)

    var = True
    while q:
        
        level = deque()
        qLen = len(q)

        for _ in range(qLen):
            node = q.popleft()
            if node:
                if var:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                q.append(node.left)
                q.append(node.right)
        
        if level:
            result.append(list(level))

        var = not var

    return result




def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
