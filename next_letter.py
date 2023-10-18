# "Find Smallest Letter Greater Than Target" on leetcode

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
       # oh this is totally different than what I was thinking. 
       # ugh. ok.
        start = 0
        end = len(letters) - 1
        smallest = ''
        while start <= end:
            mid = start + (end-start) // 2
            curr = letters[mid]
            if curr == target or curr < target:
                # too small, need to increase start
                start = mid + 1
            else:
                # greater than target
                if smallest == '':
                    smallest = curr
                elif curr < smallest:
                    smallest = curr
                end = mid - 1
            
        if smallest != '':
            return smallest
        return letters[0]

        

if __name__ == "__main__":
    s = Solution()
    print(s.nextGreatestLetter(["c","f","j"], 'a'))
    print(s.nextGreatestLetter(["c","f","j"], 'c'))
    print(s.nextGreatestLetter(["x","x","y","y"], 'z'))