from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # why am I having so much difficulty with this. ugh
        n1 = len(s)
        n2 = len(t)
        if n2 > n1:
            return ""
        elif n2 == n1:
            return s if Counter(t) == Counter(s) else ""

        c = Counter(t)
        l = r = 0
        sml = n1 + 1
        ind = -1 

        while r < n1:
            if s[r] in c:
                c[s[r]] -= 1

            while ((s[l] not in c) or (s[l] in c and c[s[l]] < 0)) and l < r:
                if s[l] in c:
                    c[s[l]] += 1
                l += 1
            if c.most_common(1)[0][1] <= 0 and r - l + 1 < sml:
                # if r - l + 1 < sml:
                sml = r - l + 1
                ind = l

            r += 1
       

        # if we never found a correct substring
        if ind == -1:
            return ""

        # otherwise ret substring of best ind
        return s[ind:ind+sml]


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("ab", "a"))