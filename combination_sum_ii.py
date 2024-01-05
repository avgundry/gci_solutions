# challenge problem for ch16

from collections import deque
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # ok...utter brute force is generate all possible combinations
        # of numbers, then see which sums work.
        # how the fuck do I do that.
        perms = []
        q = deque()
        q.append([])
        for num in candidates:
            currlen = len(q)
            while q:
                curr = q.pop()
                curr.append(num)




if __name__ == "__main__":
    s = Solution()
