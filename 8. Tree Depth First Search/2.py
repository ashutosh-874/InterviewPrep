# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):

    result = []

    def dfs(node, curSum, arr):
        
        if not node:
            return
        
        curSum += node.val
        arr.append(node.val)

        if not node.left and not node.right:
            if curSum == sum:
                result.append(arr)
        
        return dfs(node.left, curSum, arr[:]), dfs(node.right, curSum, arr[:])

    dfs(root, 0, [])
    return result




def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()
