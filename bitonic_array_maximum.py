from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1 

        # binary search until finding num whose adjacent indices are both less than it
        # O(log(n))
        while start <= end:
            mid = (start + end) // 2
            curr = arr[mid]
            if mid == 0:
                mid += 1
            elif mid == len(arr):
                mid -= 1
            if arr[mid - 1] < curr:
                if arr[mid + 1] < curr:
                    return mid 
                else:
                    start = mid + 1
            else:
                end = mid - 1

        # nothing found
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.peakIndexInMountainArray([0, 1, 0]))
    print(s.peakIndexInMountainArray([3,9,8,6,4]))