# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


class Solution:
    class TreeNode:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def goodNodes(self, root):
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, float("-inf"))


def main():
    s = Solution()
    tree = s.TreeNode(2)
    three = s.TreeNode(3)
    four = s.TreeNode(4)
    five = s.TreeNode(5)
    one = s.TreeNode(1)
    seven = s.TreeNode(7)

    tree.left = three
    tree.right = four
    three.left = five
    three.right = one
    four.right = seven

    print(s.goodNodes(tree))


main()
