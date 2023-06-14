from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # hopefully optimal solution
        i = 0 
        merged = False
        if len(intervals) == 0:
            return [newInterval]
        while i in range(len(intervals)):
            # this will only occur in the case that there is NOT overlap...
            # ugh, no it won't, cause we're only looking at a single interval.
            interval = intervals[i]
            if newInterval[0] <= interval[1]:
                if newInterval[1] < interval[0]:
                    # it's just completely less than interval in this case.
                    # god I am tired.
                    intervals.insert(i, newInterval)
                    return intervals
                # else in this case, newInterval[1] >= interval[0]...so there IS some overlap.
                else:
                    intervals[i] = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
                    merged = True

                    j = i + 1
                    curr = intervals[i]
                    while j in range(i+1, len(intervals)):
                        # merge the rest if needed.
                        if curr[1] >= intervals[j][0]:
                            intervals[i] = [min(curr[0], intervals[j][0]), max(curr[1], intervals[j][1])] 
                            del intervals[j]
                            #j += 1
                        else:
                            return intervals
                        
            
            i += 1

        if i == len(intervals) and merged == False:
            intervals.append(newInterval)
        
        return intervals





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
    s3 = Solution()
    s4 = Solution()
    s5 = Solution()
    print(s1.insert([[1,3], [6,9]], [2, 5]))
    print(s2.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print(s3.insert([], [1, 2]))
    print(s4.insert([[1, 5]], [2, 3]))
    print(s5.insert([[1, 5]], [6, 8]))