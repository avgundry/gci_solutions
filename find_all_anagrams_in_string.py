from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = [] 
        n = len(s)
        n2 = len(p)
        c = Counter(p)

        for i in range(n):
            if i >= n2:
                c[s[i - n2]] += 1
            c[s[i]] -= 1
            if c.most_common(1)[0][1] == 0:
                ans.append(i - n2 + 1)

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", p = "abc"))