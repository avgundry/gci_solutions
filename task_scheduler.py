from collections import Counter
from heapq import *
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # if the wait time is 0, we can do any permutation.
        if n == 0:
            return len(tasks)

        # Maybe...two stacks? 
        # One organized by wait time remaining, one organized by
        # most elements?
        # or...no, just one heap? hmmm does that work?
        # yeah and just negate count remaining...
        counts = Counter(tasks)
        
        heap = []
        for task, count in counts.items():
            heappush(heap, [0, -count, task])
        # print(heap)

        time = 0
        # while there are still tasks left
        while heap:
            # since it's ordered by wait time,
            # the first elem will always have the smallest wait
            # time of the whole heap

            while heap[0][1] == 0:
                # if it has no tasks remaining we pop it and start again
                heappop(heap)
                if not heap:
                    return time
            # if the first elem has no wait time we use it
            if heap[0][0] == 0:
                # suboptimal
                curr = heappop(heap)
                heappush(heap, [curr[0] + n + 1, curr[1] + 1, curr[2]])

            # no matter what, always increment time each step
            time += 1

            # naive method; decrement wait time for each task
            # possible way to optimize is use auxiliary storage for 
            # tasks with >0 wait time, then decrement that each loop,
            # which is O(n) 
            for i in range(len(heap)):
                if heap[i][0] > 0:
                    heap[i][0] -= 1
            heapify(heap)
        #     print(f"heap now: {heap}\n")

        # print('\n')
        return time


        # print(heap)

        


        """poor runtime hashmap implementation - exceeds time limit"""
        # counts = Counter(tasks)
        # # then also have a map of how long we must wait for each task.
        # waits = {task: 0 for task in set(tasks)}
        # # waits = dict(zip(tasks, [0 for _ in range(len(tasks))]))
        # time = 0

        # # while tasks are remaining
        # while counts.total() > 0:
        #     # find the most common element remaining that we can still
        #     # place.
        #     most_common = None
        #     for task, count in counts.most_common():
        #         if waits[task] == 0:
        #             most_common = task
        #             break
        #     if most_common != None:
        #         # we found a task we could use
        #         counts[most_common] -= 1
        #         waits[most_common] += n + 1
        #     # If we didn't we still have to idle.
        #     time += 1
        #     for i in waits:
        #         if waits[i] > 0:
        #             waits[i] -= 1
        #     counts = +counts
            

        # return time




if __name__ == "__main__":
    s = Solution()
    print(s.leastInterval(["A","A","A","B","B","B"], 2))
    print(s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))

        