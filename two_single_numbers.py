# "Single Number III" on Leetcode.

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        y1 = 0
        for num in nums:
            y1 ^= num

        # now y1 = x_j ^ x_k, where x_j,x_k are the unique numbers.
        
        rightmost_bit = 1
        # find the rightmost bit in y1 that is equal to 1.
        while (y1 & rightmost_bit) == 0:
            rightmost_bit = rightmost_bit << 1
        
        # After the loop, we will have found it. Then, XOR numbers 
        # based on the value of this bit to find each target number.
        num1 = num2 = 0
        for num in nums:
            if (rightmost_bit & num) == 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]

                 
        

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([1,2,1,3,2,5]))
    print(s.singleNumber([0,1,2,2]))