from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # just bucket sort

        i = 0
        while i < len(nums):
            # print(f"current ind: {i} and nums: {nums}")
            if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == nums[nums[i] - 1]:
                i += 1
            else:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp


        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return i + 1

        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1,2,0]))
    print(s.firstMissingPositive([3,4,-1,1]))
    print(s.firstMissingPositive([7,8,9,11,12]))