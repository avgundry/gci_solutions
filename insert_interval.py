from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # hopefully optimal solution
        i = 1
        newInterEnd = newInterval[1]

        # "brute" force - simply inserts then reimplements previous solution to merge_intervals.
        # suboptimal, but still O(n) time and O(1) space?
        # Ah. No. It's O(n*log(n)) due to the sort. Darn.
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        start_ind = 0
        start = intervals[0][0]
        end = intervals[0][1]

        while i in range(1, len(intervals)):
            interval = intervals[i]
            # slight optimization of brute force
            if newInterval[1] < interval[0]:
                break
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                # merge the intervals
                intervals[start_ind] = [start, end]
                # delete all merged intervals
                del intervals[start_ind + 1:i]
                i -= i - start_ind
                start_ind = i + 1
                start = interval[0]
                end = interval[1]

            i += 1

        intervals[start_ind] = [start, end]
        del intervals[start_ind+1:i]
        
        # while i < len(intervals):
        #     interval = intervals[i]
        #     if back < interval[0]:
        #         # we will not go any farther, in this case. 
        #         if i == 0:
        #             # if we're at the start of the list, simply insert it here.
        #             intervals.insert(0, newInterval)
        #             break
        #         elif front < interval[i - 1]:
        #             #



        # # implementation of brute force solution with a check to see if we can stop merging.
        # i = 1
        # newInterEnd = newInterval[1]

        # intervals.append(newInterval)
        # intervals.sort(key=lambda x:x[0])
        # start_ind = 0
        # start = intervals[0][0]
        # end = intervals[0][1]

        # while i in range(1, len(intervals)):
        #     interval = intervals[i]
        #     if newInterval[1] < interval[0]:
        #         break
        #     if interval[0] <= end:
        #         end = max(interval[1], end)
        #     else:
        #         # merge the intervals
        #         intervals[start_ind] = [start, end]
        #         # delete all merged intervals
        #         del intervals[start_ind + 1:i]
        #         i -= i - start_ind
        #         start_ind = i + 1
        #         start = interval[0]
        #         end = interval[1]

        #     i += 1

        # intervals[start_ind] = [start, end]
        # del intervals[start_ind+1:i]


        # return intervals

        ############################################################
        # "brute" force - simply inserts then reimplements previous solution.
        # suboptimal, but still O(n) time and O(1) space.
        # i = 1
        # newInterEnd = newInterval[1]

        
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x:x[0])
        # start_ind = 0
        # start = intervals[0][0]
        # end = intervals[0][1]

        # while i in range(1, len(intervals)):
        #     interval = intervals[i]
        #     if interval[0] <= end:
        #         end = max(interval[1], end)
        #     else:
        #         # merge the intervals
        #         intervals[start_ind] = [start, end]
        #         # delete all merged intervals
        #         del intervals[start_ind + 1:i]
        #         i -= i - start_ind
        #         start_ind = i + 1
        #         start = interval[0]
        #         end = interval[1]

        #     i += 1

        # intervals[start_ind] = [start, end]
        # del intervals[start_ind+1:i]


        # return intervals
    
if __name__ == "__main__":
    s1 = Solution()
    s2 = Solution()
    print(s1.insert([[1,3], [6,9]], [2, 5]))
    print(s2.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))