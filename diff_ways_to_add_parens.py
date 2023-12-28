from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # oh ok. We aren't permuting the expression, only parentheses.
        # that's significantly easier.
        # hm. brute force approach is to get all possible permutations
        # of parentheses locations, and then evaluate each and every 
        # value of those.
        perms: List[str] = []
        perms_c: List[str] = []
        self.recurseOpens(expression, perms, 0)
        for perm in perms:
            self.recurseClosed(perm, perms_c, len(perm) - 1, perm.count('('))
        # perms: List[str] = self.permutations(expression)
        # print(perms)
        print(len(perms)) # for 3 should be 2^3, so 8 ? welp yeah 32 is way too many.
        print(perms_c)
        return perms

    def recurseOpens(self, expression, perms, ind):
        # get all possible places we can place an open parenthesis
        if ind >= len(expression):
            perms.append(expression)
        else:
            if expression[ind] not in ['+', '-', '*']:
                self.recurseOpens(expression[:ind] + '(' + expression[ind:], perms, ind + 2)
            self.recurseOpens(expression, perms, ind + 1)

        
    def recurseClosed(self, expression, perms, ind, opn):
        if ind == 0:
            for i in range(opn):
                expression += ')' 
            perms.append(expression)
        else:
            if expression[ind] not in ['+', '-', '*', '(']:
                if opn == 0:
                    perms.append(expression)
                for i in range(opn):
                    self.recurseClosed(expression[:ind + 1] + ')' * i + expression[ind+1:], perms, ind - i - 1, opn - i)
            else:
                self.recurseClosed(expression, perms, ind - 1, opn)

    def recursePerms(self, expression, perms, ind, opn):
        if ind >= len(expression) - 1:
            for i in range(opn):
                expression += ')'
            perms.append(expression)
        # elif ind == len(expression) - 1:
        #     for i in range(opn):
        #         expression += ')'
        else:
            if expression[ind] not in ['+', '-', '*', '(', ')']:
                self.recursePerms(expression[:ind] + '(' + expression[ind:], perms, ind + 2, opn + 1)
                if opn > 0:
                    self.recursePerms(expression[:ind+1] + ')' + expression[ind+1:], perms, ind + 1, opn - 1)
                self.recursePerms(expression, perms, ind + 1, opn)

    
        
    def eval(self, num1: int, num2: int, op: str):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        else:
            raise Exception("invalid op provided")


if __name__ == "__main__":
    s = Solution()
    print(s.diffWaysToCompute("2-1-1"))