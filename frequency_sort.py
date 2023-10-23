# "Sort Characters by Frequency" on Leetcode

import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        # this seems exactly the same as the last problem?

        c = collections.Counter(list(s))

        print(''.join([x[0]*x[1] for x in c.most_common()]))



if __name__ == "__main__":
    s = Solution()
    s.frequencySort("tree")
