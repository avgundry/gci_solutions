from collections import Counter
from heapq import *


class Solution:
    def reorganizeString(self, s: str) -> str:
        # Hm. 
        # Do we use a heap here?? Hm...

        # O(n) to turn it into a counter.
        c = Counter(s)
        newstr = []


        prev = ''
        curr = c.most_common(1)[0][0]
        while c.total() != 0:
            if prev == curr:
                if len(list(c)) == 1:
                    return ""
                curr = c.most_common(2)[1][0]
            else:
                prev = curr
                newstr.append(curr)
                c[curr] -= 1
                curr = c.most_common(1)[0][0]
            c = +c

        if c.total() > 0:
            return ""

        print(newstr)
        return ''.join(newstr)

if __name__ == "__main__":
    s = Solution()
    print(s.reorganizeString('aab'))
    print(s.reorganizeString('aaaab'))

            
