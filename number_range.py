from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        found = found_start = found_end = -1 
        start = 0
        end = len(nums) - 1

        # inefficient brute force solution w/ no optimizations
        # stil O(3log(n))

        # binary search until finding *any* occurrence of the target.
        while start <= end and found == -1:
            mid = (start + end) // 2
            if nums[mid] == target:
                found = mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        # if target isn't found: return [-1, -1]
        if found == -1:
            return [-1, -1]

        # binary search in front of found and behind found
        # for front: if num[front] == target and front == 0 or num[front - 1] != target, we've found front
        # same for back but inverted
        if found == 0:
            found_start = found
        if found == len(nums) - 1:
            found_end = found

        # two separate loops since doing inefficient solution
        left = 0
        right = found 
        while left <= right and found_start == -1:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                # found front
                found_start = mid 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = found 
        right = len(nums) - 1 
        while left <= right and found_end == -1:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target):
                # found end 
                found_end = mid 
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1 


        return [found_start, found_end]

if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))
    print(s.searchRange([5,7,7,8,8,10], 6))
    print(s.searchRange([], 0))
    print(s.searchRange([2,2], 2))