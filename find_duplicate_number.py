from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # cyclic sort the list first
        i = 0
        while i in range(len(nums)):
            num = nums[i]
            if num == i + 1:
                i += 1
            else:
                num2 = nums[i - 1]
                if nums[num - 1] == num:
                    # there's a duplicate and we found the number
                    return num
                else:
                    # otherwise swap
                    nums[i], nums[num - 1] = nums[num - 1], nums[i]


if __name__ == "__main__":
    s1 = Solution()
    assert s1.findDuplicate([1,3,4,2,2]) == 2
    assert s1.findDuplicate([3,1,3,4,2]) == 3