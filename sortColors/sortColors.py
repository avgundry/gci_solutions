from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # simply add up the number then change nums accordingly??
        zeros = 0
        ones = 0
        twos = 0

        for num in nums:
            match num:
                case 0:
                    zeros += 1
                case 1:
                    ones += 1
                case 2:
                    twos += 1
        
        # print(f"zeros, ones, twos (respectively): {zeros}, {ones}, {twos}")
        # print(f"nums before sorting: {nums}")
        for i in range(zeros):
            nums[i] = 0
        # print(f"nums after zeros: {nums}")
        for i in range(zeros, zeros + ones):
            # print(f"switching index {i} to 1")
            nums[i] = 1
        # print(f"nums after ones: {nums}")
        for i in range(zeros + ones, zeros + ones + twos):
            nums[i] = 2
        # print(f"nums after twos: {nums}")
        
        # print(nums)

if __name__ == "__main__":
    s = Solution()
    s.sortColors([2,0,2,1,1,0])
    s.sortColors([2,0,1])