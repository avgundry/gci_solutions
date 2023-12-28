from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Basically, binary search to find the point in the array where
        # it becomes monotonically increasing - the original start of
        # the array.

        left = 0
        right = len(nums) - 1
        prev = -1

        while left <= right:
            mid = (left + right) // 2
            
            # In this case, we've found the original start of the arr.
            if nums[mid] > nums[mid + 1]:
                left = right + 1
            # In this case, we have passed the original start.
            elif nums[mid] < nums[prev]:
                right = mid - 1
            # Otherwise, the original start is further to the right.
            else:
                left = mid + 1

            prev = mid

        # Mid will now be the index of the original start of the array.

        # In this case, the target will be between index 0 and mid, so
        # we just binary search that range for it.
        if nums[mid] > target and nums[0] < target:
            left = 0
            right = mid
        # Otherwise, search the other half of the array.
        else:
            left = mid
            right = len(nums) - 1

        # Then search and return the index, or -1 if not found.
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))
