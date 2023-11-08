from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)

        if len(s1) > n:
            return False

        left = 0
        right = len(s1)
        c = Counter(s1)
        x = Counter(s2[left:right])
        print(c)
        print(x)
        
        if c <= x:
            return True

        # O(n) time, O(1) memory
        while right < n:
            x[s2[right]] += 1
            x[s2[left]] -= 1
            if c <= x:
                return True

            right += 1
            left += 1

        return c <= x


        

if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))
    print(s.checkInclusion("ab", "eidboaoo"))
    print(s.checkInclusion("adc", "dcda"))