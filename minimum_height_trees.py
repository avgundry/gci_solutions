from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Hm. Ok, first we must topsort the tree, i.e. edges, I guess.
        self.topsort(n, edges)

    def topsort(self, n, edges):
        graph = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]
        trees = []

        for x, y in edges:
            graph[x].append(y)

        trees = []
        # For each possible root...iterate over ways to go out from it?
        for i in range(len(graph)):
            self.topsortHelper(graph, visited, i, trees, [])
            # if not self.topsortHelper(graph, visited, i):
            #     return 0 # only in bizarre case that the 'tree' has a loop.
            #     # yeah idk what I'm doing here :\
        print(trees)

    def topsortHelper(self, graph, visited, i, trees, tree):
        if visited[i] == -1:
            # cycle exists in the loop
            return False
        print(tree)
        if len(tree) == len(graph):
            # we've visited all nodes
            trees.append(tree)
            return

        # if visited[i] == 1:
        #     return True
        
        # mark as visiting
        visited[i] == -1

        for y in graph[i]:
            if not self.topsortHelper(graph, visited, y, trees, tree):
                return False
        
        tree.append(i)
        visited[i] = 1
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))