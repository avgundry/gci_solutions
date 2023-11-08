from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # this one certainly looks...rough.
        # maybe we start with the widest possible range, and then shrink it down? 
        if len(nums) == 1:
            return [nums[0], nums[0]]

        ranges = []
        for num in nums[0]:
            ranges.append([num, num])

        ranges = self.smallest(nums, ranges, 1)

    def smallest(self, nums, ranges, ind):
        # minimize each range using numbers in nums[ind]
        for r in ranges:
            smallest_diff = abs(r[1] - r[0])
            for num in nums[ind]:
                smallest_diff = min(smallest_diff, abs(min(r[0], num) - max(r[0], num)))

        print(smallest_diff)
        
if __name__ == "__main__":
    s = Solution()
    nums1 = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    print(s.smallestRange(nums1))