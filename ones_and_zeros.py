# not technically in grokking, but in the github repo I'm using to work through the problems.
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # hm.
        # This is DP...
        # breaking it into subproblems. let's say...maxForm(strs[i:]) is the
        # max subset of strs from the ith string onwards.
        # do two sets of DP. optimize over intervals for m, then n? then intersect..?
        # no, that could theoretically not work
        # dp = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(len(strs))]
        dp = dict()
        return self.maxF(strs, m, n, 0, dp)

    def maxF(self, strs, m, n, ind, dp):
        # we are at the end of the list
        if ind >= len(strs):
            return 0
        curr = strs[ind]

        if dp.get((m, n, ind)) != None:
            if dp[(m, n, ind)] != -1:
                return dp[(m, n, ind)]


        if m >= strs[ind].count('0') and n >= strs[ind].count('1'):
            dp[(m, n, ind)] = max(
                1 + self.maxF(strs, m - strs[ind].count('0'), n - strs[ind].count('1'), ind + 1, dp),
                self.maxF(strs, m, n, ind + 1, dp)
            )
        else:
            dp[(m, n, ind)] = self.maxF(strs, m, n, ind + 1, dp)

        return dp[(m, n, ind)]


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxForm(["10","0001","111001","1","0"], m=5, n=3)) # should be 4