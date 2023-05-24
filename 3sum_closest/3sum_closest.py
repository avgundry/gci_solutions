# leetcode problem: https://leetcode.com/problems/3sum-closest/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # set the closest to...something. Maybe sum of first three.
        # do same as three sum, but use < target and > target to move things
        # whenever I have a sum smaller than closest, update closest
        # hmm. will loop over EVERYTHING - after doing so, return closest
        sums = set()
        n = len(nums)
        nums.sort()
        closest = float('inf')

        # loop to second-to-last value, since we need 3 total
        # O(n - 2)
        for i in range(n - 2):
            # O(1)
            slow_num = nums[i]
            left = i + 1
            right = n - 1

            # O(n)...? 
            # Really this goes from index 1 to n at worst; so n - 1 in the case there's only 3 numbers; so O(n)
            while left < right:
                curr_sum = slow_num + nums[left] + nums[right]
                # first, check if the current sum is smaller.
                if abs(target - curr_sum) < abs(target - closest): 
                    closest = curr_sum
                # smaller than target, so increment left
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                # if our current sum is the target just return it.
                else:
                    return curr_sum

        return closest

if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4], 1))
    print(s.threeSumClosest([0,0,0], 1))