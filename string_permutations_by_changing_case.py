# Letter Case Permutation on leetcode

from collections import deque
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # GTCI 'proper' solution
        # nevermind - I mistyped the code. sigh
        perms = []
        perms.append(s)
        for i in range(len(s)):
            if s[i].isalpha():
                n = len(perms)
                for j in range(n):
                    chs = list(perms[j])
                    chs[i] = chs[i].swapcase()
                    perms.append(''.join(chs))

        return perms


        # each letter is either uppercase or lowercase.
        # so a can be a or A. two permutations.
        # ab can be ab or Ab or aB or AB. four permutations. 
        # abc can be abc, abC, aBc, Abc, aBC, AbC, ABc, ABC. 8 permutations.
        # we can see it's 2^n permutations where n is number of letters. 
        # we do NOT include numbers, obviously.

        # my solution
        # perms = deque()
        # perms.append('')

        # for letter in s:
        #     p_len = len(perms)
        #     for _ in range(p_len):
        #         p = perms.popleft()
        #         if letter.isalpha():
        #             perms.append(p + letter.lower())
        #             perms.append(p+letter.upper())
        #         else:
        #             perms.append(p+letter)
        
        # return perms

if __name__ == "__main__":
    s = Solution()
    print(s.letterCasePermutation("a1b2"))


        