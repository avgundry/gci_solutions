from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Hmm. Work backwards maybe? 
        # Brute force is to start with rightmost thing, check if it's bigger than every number before it
        # If not, that's the start of our window
        # continually update left every time we find a num that is bigger than all numbers that come before it
        # (in normal left-to-right order)

        # I guess working backwards or forwards is not relevant, here
        # O(n) could look something like putting elems in a hash map first...shrug
        """
        O(n) time, O(1) space solution.
        """
        n = len(nums)
        if n == 1 or n == 0:
            return 0
        
        # first, simply find the first location where i < j but a[i] > a[j]
        # i.e. the first inversion.
        left = 0
        while left < n - 1:
            if nums[left] > nums[left + 1]:
                break
            left += 1

        # then...hmmm. need to find the largest index left such that any(nums[left] < )
        high = -float('inf')
        high_ind = 0
        right = left
        while right < n:
            if nums[right] > high:
                high = nums[right]
                high_ind = right
            right += 1
        
        if right == left or high_ind == n - 1:
            return 0

        return right - left + 1

        return 0

        """
        This isn't clean at all. However, it runs in O(n) time and space.
        """
        n = len(nums)
        if n == 1 or n == 0:
            return 0

        # index i contains the largest number in nums[:i + 1].
        highest_arr = [-float('inf') for _ in range(n)]
        high = -float('inf')
        for i in range(n):
            high = max(high, nums[i])
            highest_arr[i] = high

        # print(highest_arr)

        # then work backwards???
        right = n - 1
        # find the rightmost edge of the subarray to start
        while right >= 0:
            if nums[right] >= highest_arr[right]:
                right -= 1
            else:
                break

        # then work forwards to find where left meets?
        # seems to necessitate a low arr
        lowest_arr = [float('inf') for _ in range(n)]
        low = float('inf')
        for i in range(n - 1, -1, -1):
            low = min(low, nums[i])
            lowest_arr[i] = low
        print(lowest_arr)
        left = 0
        while left <= right:
            if nums[left] <= lowest_arr[left]:
                left += 1
            else:
                break

        print(nums[left:right])
        if left == right:
            return 0

        return right - left + 1

if __name__ == "__main__":
    s = Solution()
    print(s.findUnsortedSubarray([2,6,4,8,10,9,15]))
    print(s.findUnsortedSubarray([1]))
