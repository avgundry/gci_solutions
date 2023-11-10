from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        if n2 > n1:
            return ""

        c = Counter(t)
        l = r = 0
        sml = n1 + 1
        ind = -1 

        while r < n1:
            if c.most_common(1)[0][1] > 0:
                if s[r] in c:
                    c[s[r]] -= 1
                r += 1
            # t is in our window
            else:
                if s[l] in c:
                    if c[s[l]] < 0:
                        c[s[l]] += 1
                        l += 1
                    else:
                        if s[r] in c:
                            c[s[r]] -= 1
                        r += 1
                else:
                    l += 1
                if r - l + 1 < sml:
                    sml = r - l + 1
                    ind = l


        if ind == -1:
            return ""

        return s[ind:ind+sml]


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
        