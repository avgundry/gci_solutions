from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)] 
        visited = [0 for _ in range(numCourses)]

        # make the graph
        for x, y in prerequisites:
            graph[x].append(y)

        # visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, ind):
        # if index node is marked as being visited, we have a loop
        if visited[ind] == -1:
            return False
        
        if visited[ind] == 1:
            return True

        # mark as visiting it
        visited[ind] == -1

        for j in graph[ind]:
            if not self.dfs(graph, visited, j):
                return False

        visited[ind] = 1
        return True