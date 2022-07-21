from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):

    if root is None:
        return None

    q = deque()
    q.append(root)

    cond = False
    while q:

        qLen = len(q)
        for _ in range(qLen):
            node = q.popleft()
            if cond:
                return node
            if node.val == key:
                cond = True
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

    





def main():
    root = TreeNode(1);
    root.left = TreeNode(2);
    root.right = TreeNode(3);
    root.left.left = TreeNode(4);
    root.left.right = TreeNode(5);

    result = find_successor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = find_successor(root, 5)
    if result:
        print(result.val)

    result = find_successor(root, 12)
    if result:
        print(result.val)


main()
