class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):



    def dfs(node, arr):

        if not node:
            return 0
        
        arr.append(node.val)

        res, curSum = 0, 0
        x = len(arr)
        for i in range(x-1, -1, -1):
            curSum += arr[i]
            if curSum == S:
                res += 1
        
        res += dfs(node.left, arr)
        res += dfs(node.right, arr)

        del arr[-1]

        return res

    return dfs(root, [])





def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
