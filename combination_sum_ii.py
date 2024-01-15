# challenge problem 1 for ch16
from collections import deque
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # I *think* that keeping an array of the possible sums at 
        # index[i] in dp[i] would work just fine.
        # I.e. dp[i] represents all possible sums of all possible 
        # subsets from index i onwards...? No...that's O(2^n) time :\
        #
        result = []
        self.recurse(candidates, 0, [], result, target)
        return result

    def recurse(self, nums, start, path, res, targ):
        # if the current path satisfies the target
        if targ == 0:
            res.append(path)
            return

        for i in range(start, len(nums)):
            # Lets us ignore duplicate elements since nums are sorted
            if i > start and nums[i] == nums[i - 1]:
                continue
            if nums[i] > targ:
                # couldn't be this
                break
            self.recurse(nums, i + 1, path + [nums[i]], res, targ - nums[i])
        
            






        # ok...utter brute force is generate all possible combinations
        # of numbers, then see which sums work.
        # This will be O(2^n) time & space.
        """Brute force solution, O(2^N) time and space"""
        # perms = deque()
        # perms.append([])
        # for c in candidates:
        #     currlen = len(perms)
        #     for i in range(currlen):
        #         curr = perms.popleft()
        #         perms.append(curr.copy())
        #         curr.append(c)
        #         curr.sort()
        #         if curr not in perms:
        #             perms.append(sorted(curr))

        # # perms = list(set(perms))
        # ret = []
        # for perm in perms:
        #     if sum(perm) == target:
        #         ret.append(perm)
        
        # return ret


if __name__ == "__main__":
    s = Solution()
    # print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    # print(s.combinationSum2([146,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12], 27))
    # print(s.combinationSum2([1], 1))
    print(s.combinationSum2([3,1,3,5,1,1], 8))
