class MountainArray:
    def __init__(self, arr):
        self.arr = arr
    def get(self, index: int) -> int:
        return self.arr[index]
    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: MountainArray) -> int:
        # begin by binary searching for the peak of the mountain.
        n = mountain_arr.length()
        start = 0
        end = n - 1
        targ_ind = -1

        while start <= end:
            mid = (start + end) // 2
            mid_val = mountain_arr.get(mid)
            # if mid_val == target:
            # account for being at edge?
            if mid_val < mountain_arr.get(mid+1):
                # in this case we are left of peak
                if mid_val == target:
                    # since we'd be left of peak it'd be what we're 
                    # looking for
                    return mid
                start = mid + 1
            elif mid_val < mountain_arr.get(mid - 1):
                # in this case we're right of the peak
                if mid_val == target:
                    targ_ind = mid
                    # it's still possible there's the target left of 
                    # the peak however so we just save for later
                end = mid - 1
            else:
                # found peak, so break loop
                start = end + 1

        # search the left half first, always
        start = 0
        end = mid
        while start <= end:
            mid2 = (start + end) // 2
            mid_val = mountain_arr.get(mid2)
            if mid_val == target:
                return mid2
            elif mid_val < target:
                start = mid2 + 1
            else:
                end = mid2 - 1
        # search the right half either until we have targ_ind or we 
        # find nothing. automatically returns targ_ind if found above
        start = mid
        end = n - 1
        while start <= end and targ_ind == -1:
            mid = (start + end) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                targ_ind = mid
            elif mid_val > target:
                start = mid + 1
            else:
                end = mid - 1

        return targ_ind

if __name__ == "__main__":
    s = Solution()
    # print(s.findInMountainArray(2, MountainArray([1,2,3,4,5,3,1])))
    print(s.findInMountainArray(2, MountainArray([1,5,2])))