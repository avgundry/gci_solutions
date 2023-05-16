from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two-pointer method. 
        triplets = set()
        nums = sorted(nums)
        # go up to the 2nd-to-last element, since we need 3 for a triplet
        for i in range(len(nums) - 1):
            number = nums[i]
            ptr1 = i+1
            ptr2 = len(nums)-1
            while (ptr1 < ptr2):
                curr_sum = number + nums[ptr1] + nums[ptr2]
                if curr_sum == 0:
                    # break and add to triplet
                    # do we break? hm
                    triplets.add((number, nums[ptr1], nums[ptr2]))
                    ptr1 += 1
                    ptr2 -= 1
                elif curr_sum < 0:
                    # need to move left ptr up.
                    ptr1 += 1
                else:
                    # need to move right ptr down.
                    ptr2 -= 1

        print(list(triplets))
        return list(triplets)


        # optimized two-ptr
        triplets = set()
        nums = sorted(nums)
        # go up to the 2nd-to-last element, since we need 3 for a triplet
        for i in range(len(nums) - 1):
            # skip duplicate values.
            if i != 0 and nums[i] == nums[i-1]:
                continue
            number = nums[i]
            ptr1 = i+1
            ptr2 = len(nums)-1
            while (ptr1 < ptr2):
                curr_sum = number + nums[ptr1] + nums[ptr2]
                if curr_sum < 0:
                    ptr1 += 1
                elif curr_sum > 0:
                    ptr2 -= 1
                else: 
                    # break and add to triplet
                    # do we break? hm
                    triplets.add((number, nums[ptr1], nums[ptr2]))
                    ptr1 += 1
                    ptr2 -= 1
                    # skip duplicates of other two
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        print(list(triplets))
        return list(triplets)


if __name__ == "__main__":
    s = Solution()
    s.threeSum([1, 1, 0, -1])
    s.threeSum([-1,0,1,2,-1,-4])
