# subsets II on leetcode

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Naive brute force solution: same as for non-duplicate subsets, but we
        # simply convert to a set at the very end
        subsets = [[]]

        for num in nums:
            j = 0
            curr_len = len(subsets)
            while j < curr_len:
                new_sub = subsets[j].copy()
                new_sub.append(num)
                new_sub.sort()
                # brute force method
                if new_sub not in subsets:
                    subsets.append(new_sub)
                j += 1

        return subsets

if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))