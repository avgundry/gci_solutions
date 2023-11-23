# no equivalent on leetcode. have to setup own cases.
# similar to finding the first missing one
from typing import List


class Solution:
    def firstKMissing(self, arr: List[int], k: int) -> int:
        # cyclic sort the arr first
        n = len(arr)
        i = 0 
        while i < len(arr):
            if arr[i] >= n or arr[i] < 0 or arr[i] == i + 1:
                i += 1
            else:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

        # will be sorted now. just loop over and add nums to array
        ret = []
        for i in range(n):
            if k <= 0:
                return ret
            if i + 1 != arr[i]:
                ret.append(arr[i])
                k -= 1


if __name__ == "__main__":
    s = Solution()
    print(s.firstKMissing([2,3,4,7,11], 2))
    print(s.firstKMissing([1,2,3,4], 3))
