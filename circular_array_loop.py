from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """Optimized O(n) time, O(1) space method"""
        # Whenever we finish a cycle, if it didn't return True, simply
        # mark all the elements in the cycle as 0. We can do this since
        # we are guaranteed that nums[i] != 0 for all i (before we
        # change it).
        n = len(nums)
        for i in range(n):
            if self.cycleFinder(n, i, nums):
                return True
            
        return False


        """O(n^2) method"""
        # Can't we just use the two-pointer method here?
        # Have a fast pointer and a slow pointer.
        # If the fast and slow meet, there must be a cycle?
        # Then, check if the cycle is all negative or all non-negative.
        # Well. The problem guarantees a cycle exists *somewhere* since
        # the list is circular. We just have to find where.
        n = len(nums)
        # O(n^2) time...
        for i in range(n):
            if self.cycleFinder(n, i, nums):
                return True
        
        return False
        
    def cycleFinder(self, n, ind, nums):
        if nums[ind] == 0:
            # We've already checked this cycle.
            return False

        slow = ind
        fast = (ind + nums[ind]) % n
        while fast != slow:
            slow = (slow + nums[slow]) % n
            fast = (fast + nums[fast]) % n
            fast = (fast + nums[fast]) % n

        # They must converge at some point. In fact I believe it's a 
        # maximum of O(2N) steps before they do?
        # Then, check if the cycle they're in is all negative or all positive.
        # At this point we're guaranteed fast == slow. So just iterate
        # one until it reaches the other again.

        # Whenever we go through a point in a cycle, mark it as 0 
        # before moving on. In this case our runtime overall is O(n)
        # Cycle is length 1 in this case, return false.
        if (fast + nums[fast]) % n == slow:
            nums[slow] = 0
            return False
        else:
            # 1 if positive, 0 if negative.
            # Guaranteed that any nums[i] != 0.
            sign = nums[slow] > 0
            nums[slow] = 0
            fast = (fast + nums[fast]) % n
            while fast != slow:
                # They aren't all of the same sign, so return False.
                temp = nums[fast]
                nums[fast] = 0
                if (temp > 0) != sign:
                    return False
                fast = (fast + temp) % n

            # If we got through the loop without returning, then 
            # there must be a valid cycle, so return True.
            return True

if __name__ == "__main__":
    s = Solution()
    # print(s.circularArrayLoop([2, -1, 1, 2, 2]))
    print(s.circularArrayLoop([1,-1,5,1,4]))
    print(s.circularArrayLoop([-2,1,-1,-2,-2]))