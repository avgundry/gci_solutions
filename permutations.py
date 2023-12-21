from collections import deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # recursively generate each possible permutation starting with
        # a given number...? perhaps? that turns it into a dp problem I
        # think.
        perms = [[]]
        for num in nums:
            q = []
            while perms:
                q.append(perms.pop())
            currlen = len(q[0]) + 1
            for perm in q:
                for i in range(currlen):
                    x = perm.copy()
                    x.insert(i, num)
                    perms.append(x)
        
        return perms


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1]))
    print(s.permute([1,2]))
    print(s.permute([1,2,3]))