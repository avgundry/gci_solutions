from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return False

        cycles = [-1 for _ in range(n)]
        for pos in range(n):
            curr = pos
            # determine cycle
            cyc = set()
            while curr not in cyc:
                cyc.add(curr)
                move = nums[curr] % n
                if move + curr >= n:
                    curr = move + curr - n
                else:
                    curr += move
            cycles[pos] = cyc

        all_same = True
        for c in cycles:
            prev = None
            for num in c:
                if prev:
                    if prev < 0 != num < 0:
                        break

                prev = num
                
            if prev < 0 == num < 0:
                return True

        return False



if __name__ == "__main__":
    s = Solution()
    print(s.circularArrayLoop([2, -1, 1, 2, 2]))