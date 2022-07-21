from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):

    q = deque()
    res = []
    q.append(root)

    while q:

        levelCount = len(q)
        sum = 0
        for _ in range(levelCount):
            node = q.popleft()
            sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        res.append(sum / levelCount)
    
    return res

    


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()







