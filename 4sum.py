from typing import List


class Solution:
    # twosum of SORTED nums
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1
        doubles = []
        while left < right:
            if left + right == target:
                doubles.add(nums[left], nums[right])
                left += 1
                right -= 1
            elif left + right > target:
                right -= 1
                doubles.add(nums[left], nums[right])
            else:
                left += 1
                doubles.add(nums[left], nums[right])


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # how in god's name. what
        # How is this possibly two pointer???? 
        # n = len(nums)
        # if n < 4:
        #     return []
        # quads = set()

        # # sorts in O(nlog(n))...ish, time?
        # nums.sort()

        # # what is this...O(n^3)???
        # for x in range(n):
        #     curr = nums[x]
        #     # literally just implements 3sum inside a loop. but...I feel like 
        #     # DP is the answer here?? lol
        #     for i in range(x+1, n):
        #         slow_num = nums[i]
        #         left = i + 1
        #         right = n - 1

        #         while left < right:
        #             if (slow_num + nums[left] + nums[right]) > target - curr:
        #                 right -= 1
        #             elif (slow_num + nums[left] + nums[right]) < target - curr:
        #                 left += 1
        #             else:
        #                 quads.add((curr, slow_num, nums[left], nums[right]))
        #                 left += 1
        #                 right -= 1

        # return quads