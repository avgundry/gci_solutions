from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x:x[0])

        # O(1) space solution
        start = intervals[0][0]
        start_ind = 0
        end = intervals[0][1]
        i = 1

        while i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                # set the interval at the start of the current block
                intervals[start_ind] = [start, end]
                # delete any merged intervals
                del intervals[start_ind+1:i]
                # I think?
                i -= i - start_ind
                
                # 
                start_ind = i + 1
                start = interval[0]
                end = interval[1]


            i += 1

        # for very last interval?
        intervals[start_ind] = [start, end]
        # delete any merged intervals
        del intervals[start_ind+1:i]

        return intervals


        # O(N) space solution
        # mergedIntervals = []
        # start = intervals[0][0]
        # end = intervals[0][1]

        # for i in range(1, len(intervals)):
        #     interval = intervals[i]
        #     if interval[0] <= end:
        #         end = max(interval[1], end)
        #     else:
        #         mergedIntervals.append([start, end])
        #         start = interval[0]
        #         end = interval[1]

        # mergedIntervals.append([start, end])

        # return mergedIntervals
   

if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))