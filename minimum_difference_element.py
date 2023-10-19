from collections import deque
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == 0:
            return []

        # O(log(n) + k) runtime.
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2 
            if arr[mid] == x:
                break
            elif arr[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        if k == 1:
            if mid + 1 >= len(arr) or abs(arr[mid] - x) <= abs(arr[mid+1] - x):
                if mid - 1 < 0 or abs(arr[mid-1] - x) > abs(arr[mid] - x):
                    return [arr[mid]]
                else:
                    return[arr[mid-1]]
            else:
                return [arr[mid+1]]

        # then add mid and numbers around mid until we have full array
        ret = deque()
        if mid == 0:
            left = mid
            right = mid + 1
        else:
            left = mid - 1
            right = mid
        while len(ret) < k:
            if left < 0:
                ret.append(arr[right])
                right += 1
            elif right >= len(arr):
                ret.appendleft(arr[left])
                left -= 1
            elif abs(arr[right] - x) < abs(arr[left] - x):
                ret.append(arr[right])
                right += 1
            # elif abs(arr[left] - arr[mid]) < abs(arr[right] - arr[mid]):
            else:
                # left hand side is smaller OR they're tied
                # on a tie we add the left
                ret.appendleft(arr[left])
                left -= 1
            
        return list(ret)

if __name__ == "__main__":
    s = Solution()
    print(s.findClosestElements([1,2,3,4,5], 4, 3))
    assert(s.findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4) == [0,1,1,1,2,3,6,7,8])
    print(s.findClosestElements([1,1,1,10,10,10], 1, 9))
    print(s.findClosestElements([1,5,10], 1, 4))
    print(s.findClosestElements([1,5,10,12,13], 1, 9))
    print(s.findClosestElements([1,3], 1, 2))