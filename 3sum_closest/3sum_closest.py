# leetcode problem: https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # set the closest to...something. Maybe sum of first three.
        # do same as three sum, but use < target and > target to move things
        # whenever I have a sum smaller than closest, update closest
        # hmm. will loop over EVERYTHING - after doing so, return closest
        sums = set()
        n = len(nums)
        nums.sort()

        # loop to second-to-last value, since we need 3 total
        for i in range(n - 2):
            slow_num = nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = slow_num + nums[left] + nums[right]
                # first, check if the current sum is smaller.
                if curr_sum
                # smaller than target, so increment left
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return sum

if __name__ == "__main__":
    s = Solution()
    s.threeSumClosest([-1,2,1,-4], 1)
    s.threeSumClosest([0,0,0], 1)