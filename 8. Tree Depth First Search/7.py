# Path with Maximum Sum (hard)#

# Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.

# A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root. The path must contain at least one node.


import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


result = 0
def find_maximum_path_sum(root):

    global result

    def dfs(node):

        global result

        if not node:
            return 0

        lftMaxSum = dfs(node.left)
        rgtMaxSum = dfs(node.right)

        lftMaxSum = max(lftMaxSum, 0)
        rgtMaxSum = max(rgtMaxSum, 0)

        localMaxSum = lftMaxSum + rgtMaxSum + node.val

        result = max(result, localMaxSum)

        return max(lftMaxSum, rgtMaxSum) + node.val

    dfs(root)
    return result



def main():
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)

    # print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)
    # root.right.left = TreeNode(5)
    # root.right.right = TreeNode(6)
    # root.right.left.left = TreeNode(7)
    # root.right.left.right = TreeNode(8)
    # root.right.right.left = TreeNode(9)
    # print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(2)
    root.left = TreeNode(-1)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


main()
