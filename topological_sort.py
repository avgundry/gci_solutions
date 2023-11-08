from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites <= 0:
            return True


        sorted_courses = []

        # initialize graph
        indeg = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        # build graph
        for prereq in prerequisites:
            parent, child = prereq[0], prereq[1]
            graph[parent].append(child)
            indeg[child] += 1

        # find all sources 
        sources = deque()
        for key in indeg:
            if indeg[key] == 0:
                sources.append(key)

        # for each source, add it to the sorted order and subtract one from
        # all of its children's in-degrees. if a child's indeg becomes 0, add
        # it to the sources queue.
        while sources:
            vertex = sources.popleft()
            sorted_courses.append(vertex)
            for child in graph[vertex]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    sources.append(child)

        return len(sorted_courses) == numCourses
        # if len(sorted_courses) != numCourses:
        #     return False
        


        
