# subsets II on leetcode

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # optimization of brute force method
        subsets = [[]]
        nums.sort()
        # where the previous number started appending
        prev = 0

        for i in range(len(nums)):
            num = nums[i]
            if i != 0 and nums[i - 1] == nums[i]:
                # in the case of duplicate, we only append to prev subsets:w
                j = prev + 1
            else:
                # not a duplicate so loop over whole list
                start = 0
            prev = len(subsets) - 1
            curr_len = prev
            for j in range(start, prev + 1):
                new_sub = subsets[j].copy()
                new_sub.append(num)
                subsets.append(new_sub)
                j += 1

        return subsets

        # Naive brute force solution
        # subsets = [[]]

        # for num in nums:
        #     j = 0
        #     curr_len = len(subsets)
        #     while j < curr_len:
        #         new_sub = subsets[j].copy()
        #         new_sub.append(num)
        #         new_sub.sort()
        #         # brute force method
        #         if new_sub not in subsets:
        #             subsets.append(new_sub)
        #         j += 1

        # return subsets

if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))