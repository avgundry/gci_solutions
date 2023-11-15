# challenge problem for ch16

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # recursive solution first I guess
        return self.recurseSum(candidates, target)


if __name__ == "__main__":
    s = Solution()
