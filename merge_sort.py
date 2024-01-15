from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    # Sorts nums[start:end]
    def mergeSort(self, nums, start, end):
        if start >= end:
            return

        mid = (start + end) // 2 
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid + 1, end)
        self.merge(nums, start, mid, end)

    def merge(self, nums, start, mid, end):
        left_len = mid - start + 1
        right_len = end - mid

        left = [nums[start + i] for i in range(left_len)]
        right = [nums[mid + i + 1] for i in range(right_len)]

        i = j = 0
        k = start
        while i < left_len and j < right_len:
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < left_len:
            nums[k] = left[i]
            i += 1
            k += 1
        while j < right_len:
            nums[k] = right[j]
            j += 1
            k += 1

    # """Quicksort"""
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     self.quickSort(nums, 0, len(nums) - 1)
    #     return nums

    # def quickSort(self, nums, start, end):
    #     if start < end:
    #         part = self.partition(nums, start, end)
    #         self.quickSort(nums, start, part - 1)
    #         self.quickSort(nums, part + 1, end)

    # def partition(self, nums, start, end):
    #     # pivot = sorted([nums[start], nums[end], nums[(start + end) // 2]])[1]
    #     pivot = nums[end]
    #     i = start - 1
    #     for j in range(start, end):
    #         if nums[j] < pivot:
    #             i += 1
    #             nums[i], nums[j] = nums[j], nums[i]

    #     nums[i + 1], nums[end] = nums[end], nums[i + 1]

    #     return i + 1


    



    """Mergesort"""
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     if len(nums) != 0:
    #         self.mergeSort(nums, 0, len(nums) - 1)
    #     return nums

    # def mergeSort(self, nums, start, end):
    #     if start >= end:
    #         return

    #     mid = (start + end) // 2
        
    #     self.mergeSort(nums, start, mid)
    #     self.mergeSort(nums, mid + 1, end)
    #     self.merge(nums, start, mid, end)

        
    # def merge(self, nums, start, mid, end):
    #     # mid += 1
    #     left_len = mid - start + 1
    #     right_len = end - mid
    #     left = [i for i in nums[start:mid+1]]
    #     right = [i for i in nums[mid+1:end+1]]
    #     print(left)
    #     print(right)
    #     print('\n')

    #     i = j = 0
    #     k = start
    #     while i < left_len and j < right_len:
    #         print(left[i])
    #         if left[i] <= right[j]:
    #             nums[k] = left[i]
    #             i += 1
    #         else:
    #             nums[k] = right[j]
    #             j += 1
    #         k += 1
        
    #     while i < left_len:
    #         nums[k] = left[i]
    #         i += 1
    #         k += 1
    #     while j < right_len:
    #         nums[k] = right[j]
    #         j += 1
    #         k += 1

    #     print(f'nums now: {nums}')

if __name__ == "__main__":
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))