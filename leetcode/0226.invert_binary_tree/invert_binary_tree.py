import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        q = collections.deque([root])
        while q:
            for i in range(len(q)):
                rem = q.popleft()

                rem.left, rem.right = rem.right, rem.left

                if rem.left:
                    q.append(rem.left)

                if rem.right:
                    q.append(rem.right)
        return root


if __name__ == "__main__":
    s = Solution()
    print(s.invertTree([4, 2, 7, 1, 3, 6, 9]))
