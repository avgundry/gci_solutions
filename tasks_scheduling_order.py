from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) <= 0:
            return [i for i in range(numCourses)]

        # are we expected to verify the graph is acyclic first?

        # begin just by topo sorting...
        srt_crses = []
        ordering = []

        indeg = {i:0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        # build graph
        for pr in prerequisites:
            parent, child = pr[0], pr[1]
            graph[parent].append(child)
            indeg[child] += 1

        # find all sources
        srcs = deque()

        for key in indeg:
            if indeg[key] == 0:
                srcs.append(key)

        while srcs:
            vx = srcs.popleft()
            ordering.append(vx)
            srt_crses.append(vx)
            for child in graph[vx]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    srcs.append(child)


        ordering.reverse()
        return ordering


if __name__ == "__main__":
    s = Solution()
    print(s.findOrder(2, [[1, 0]]))
    print(s.findOrder(1, []))

        