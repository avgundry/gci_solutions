# simply "Binary Search" on leetcode. somewhat dissimilar but should be close enough.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # naive straightforward method for log-n, no optimizations
        # to optimize we could check endpoints first as those take the most
        # time to reach, and then recurse if not found there
        # to optimize further: use start and end, don't pass back and forth arrays etc
        
        mid = len(nums) // 2
        # What is our base case? We have two. One is we find the target.
        if nums[mid] == target:
            return mid
        elif len(nums) == 1:
            return -1
        elif nums[mid] < target:
            # search for target in upper half of nums
            x = self.search(nums[mid:], target)
            if x == -1:
                return -1
            else:
                return mid + x
        else:
            # search for target in lower half of nums
            x = self.search(nums[:mid], target)
            if x == -1:
                return -1
            else:
                return mid - (len(nums[:mid]) - x)

         
        

if __name__ == "__main__":
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 9))
    print(s.search([-1,0,3,5,9,12], 2))
    print(s.search([1], 0))
    print(s.search(sorted([10, 5, 0, 1, 71, 12, 0, -2] * 100), -2))
    print(s.search([-1,0,3,5,9,12], 13))