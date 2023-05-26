from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # METHOD ONE - two passes
        """ simply add up the number then change nums accordingly??
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
        # print(f"nums after twos: {nums}") """
        
        # METHOD TWO - one pass
        zero_ptr = 0
        two_ptr = len(nums) - 1
        print(f"ORIGINAL nums: {nums}")
        i = 0

        while i <= two_ptr:
            match nums[i]:
                case 0:
                    nums[i] = nums[zero_ptr]
                    nums[zero_ptr] = 0
                    zero_ptr += 1
                    print(f"case zero, zero_ptr at index {zero_ptr}, nums: {nums}")
                case 2:
                    nums[i] = nums[two_ptr]
                    nums[two_ptr] = 2
                    two_ptr -= 1
                    print(f"case 2, two_ptr at index {two_ptr}, nums: {nums}")
                case _:
                    print(f"case 1, nums: {nums}")
            i += 1

        print(f"\nEND nums: \n\n {nums}\n")

if __name__ == "__main__":
    s = Solution()
    s.sortColors([2,0,2,1,1,0])
    s.sortColors([2,0,1])