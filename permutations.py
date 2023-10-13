from collections import deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numslen = len(nums)

        # create list of perms as a dq
        perms = deque()

        # have an empty list added at the start, to extend upon.
        perms.append([])

        # for each number, create permutations from it
        for num in nums:
            n = len(perms)
            for _ in range(n):
                # pop EVERY old perm out, one by one
                old_perm = perms.popleft()

                # once we have it, we begin inserting into it to create new perms
                for j in range(len(old_perm) + 1):
                    new_perm = list(old_perm)
                    new_perm.insert(j, num)
                    perms.append(new_perm)
        
        return list(perms)
    
    def fact(self, num):
        ret = 1
        for i in range(2, num + 1):
            ret *= i
        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.permute([1]))
    print(s.permute([1,2]))
    print(s.permute([1,2,3]))