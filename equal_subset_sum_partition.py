from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # basically, must find a subset such that sum(subset) = sum(nums) // 2
        # If we can't cleanly divide sum(nums) by 2 it clearly can't exist
        s = sum(nums)
        if s % 2 != 0:
            return False

        # Now...what are the subproblems?
        # I suppose there's two things we carry forward:
        # the target, and the index.
        # So we should check whether we can reach the given target from
        # a given index. This means we need a 2d DP index for the 
        # top-down method? Outer dim is index, inner is target.
        # Our target here is reaching s // 2.
        targ = s // 2
        # The bottom up approach is to have a dp where outer dim is ind
        # and inner is target; each index can reach the targets 0 and
        # nums[index]; so set dp for those to true.
        dp = [[False for i in range(targ + 1)] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
            if nums[i] <= targ:
                dp[i][nums[i]] = True

        # That sets up the dp...then from there...hm.
        # I guess...start at index 1. If dp[ind-1][target - nums[ind]]
        # is true, then we can reach it from there
        # and obviously adding the two together lets us reach the targ?
        for i in range(1, len(nums)):
            curr = nums[i]
            for j in range(targ + 1):
                # then no need to check
                if dp[i-1][j]:
                    dp[i][j] = True
                elif curr <= j and dp[i - 1][j - curr]:
                    dp[i][j] = True
        
        # The last index of each dimension is our target, i.e. whether
        # we can reach the target sum by the final index of nums.
        return dp[-1][-1]
        if dp[-1][-1] == None or dp[-1][-1] == False:
            return False
        else:
            return True
        return dp[-1][-1]

    def recurse(self, nums, ind, targ, dp):
        # If we're out of bounds just return.
        if targ == 0:
            return True
        n = len(nums)
        if ind >= n or n == 0:
            return False

        if dp[ind][targ] == None:
            # then must determine whether we can reach given target
            # from the current index.
            if nums[ind] <= targ:
                if self.recurse(nums, ind + 1, targ - nums[ind], dp):
                    dp[ind][targ] = True
                    return True
                    
            # after excluding current number
            dp[ind][targ] = self.recurse(nums, ind + 1, targ, dp)
            


        return dp[ind][targ]
        

        
        


        # partition_diffs = set()
        # partition_diffs.add(nums[0])
        # partition_diffs.add(-nums[0])


        # for i in range(1, len(nums)):
        #     # calculate the partition differences 
        #     # partition_diffs.append([0] * len(partition_diffs[i-1]) * 2)
        #     # for j in range(i):
        #     #     print(partition_diffs[i - 1])
        #     curr = nums[i]
        #     curr_lvl = set()
        #     for diff in partition_diffs:
        #         curr_lvl.add(diff + curr)
        #         curr_lvl.add(diff - curr)
        #     partition_diffs = curr_lvl

        # return 0 in partition_diffs


if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1, 2, 3])) # true
    print(s.canPartition([1,2,3,4,5,6,7])) # true
    print(s.canPartition([1,2,5])) # false
    print(s.canPartition([1, 5, 11, 5])) # true
    print(s.canPartition([1,2,3,5])) # false
