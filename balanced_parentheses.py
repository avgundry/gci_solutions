# "Generate Parentheses" on leetcode.

from collections import deque
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return
        
        class ParenStr:
            def __init__(self, st, open_pars, close_pars):
                self.st = st
                self.open = open_pars
                self.close = close_pars
        
        result = []
        perms = deque()
        perms.append(ParenStr('', 0, 0))

        while perms:
            curr = perms.popleft()

            # we have reached n full parentheses and can append to result
            if curr.open == n and curr.close == n:
                result.append(curr.st)
            else:
                if curr.open < n:
                    # if we can, add an opening parentheses
                    perms.append(ParenStr(curr.st + '(', curr.open + 1, curr.close))
                if curr.close < curr.open:
                    perms.append(ParenStr(curr.st + ')', curr.open, curr.close + 1))

        return result
            





        # this question is extremely poorly asked on leetcode - ordering should
        # not matter. this produces a valid set of parens but ordering is diff 
        # so it's not counted.
        # brute force-ish method
        # perms = deque()
        # perms.append('')
        #
        # 
        # for i in range(n):
        #     plen = len(perms)
        #     for j in range(plen):
        #         curr = perms.popleft()
        #         new_pars = list(set([f'({curr})', f'{curr}()', f'(){curr}']))
        #         perms.extend(new_pars)

        # return list(perms)

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(1))
    print(s.generateParenthesis(2))
    print(s.generateParenthesis(3))