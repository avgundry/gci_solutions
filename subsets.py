from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]

        # believe this is O(n^2) technically
        # more strictly I think it's (O^((n^2 - n))/2)?
        # but doubles every time so - possibly O(2^n)
        for num in nums:
            i = 0
            currlen = len(sets)
            while i < currlen:
                new_subset = sets[i].copy()
                new_subset.append(num)
                sets.append(new_subset)
                i += 1
            
        return sets

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3]))

