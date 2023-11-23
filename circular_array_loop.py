from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        fast = slow = 0
        fast = (fast + nums[fast]) % n
        first_neg = nums[0] < 0
        same_sign = True
        # oh my god
        while fast != slow:
            if nums[slow] < 0 != first_neg:
                same_sign = False
            slow = (slow + nums[slow]) % n
            if nums[fast] < 0 != first_neg:
                same_sign = False
            fast = (fast + nums[fast]) % n
            if nums[fast] < 0 != first_neg:
                same_sign = False
            fast = (fast + nums[fast]) % n

        if fast != 0:
            # cycle of len 1
            if (fast + nums[fast]) % n == fast or not same_sign:
                return False
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.circularArrayLoop([-2,1,-1,-2,-2]))     # should be false.

