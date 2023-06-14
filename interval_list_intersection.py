from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # init vars; A is firstList, B is secondList
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        i = j = 0
        interA = firstList[i]
        interB = secondList[j]
        intersections = []
        #intersected = False

        # loop through, checking for intersections, while we are within bounds.
        while i < len(firstList) and j < len(secondList):
            interA = firstList[i]
            interB = secondList[j]
            intersected = False
            if interB[0] <= interA[1] and interB[0] >= interA[0]:
                lower = interB[0]
                intersected = True
            elif interA[0] <= interB[1] and interA[0]>= interB[0]:
                lower = interA[0]
                intersected = True
            else:
                # increment smaller ptr and associated interval
                if interB[1] < interA[0]:
                    # B is smaller
                    j += 1
                else:
                    # A is smaller
                    i += 1

            if intersected:
                upper = min(interA[1], interB[1])
                intersections.append([lower, upper])
                if interA[1] <= interB[1]:
                    i += 1
                else:
                    j += 1
                    
        #print(intersections)

        return intersections

if __name__ == "__main__":
    s = Solution()
    assert s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]) \
        == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]