import collections
from typing import Collection, List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        partition_diffs = collections.deque()
        partition_diffs.append(nums[0])
        partition_diffs.append(-nums[0])


        for i in range(1, n):
            # calculate the partition differences 
            # partition_diffs.append([0] * len(partition_diffs[i-1]) * 2)
            # for j in range(i):
            #     print(partition_diffs[i - 1])
            curr = nums[i]
            curr_len = len(partition_diffs)
            for j in range(curr_len):
                pop = partition_diffs.popleft()
                partition_diffs.append(pop + curr)
                partition_diffs.append(pop - curr)

            print(partition_diffs)

        return 0 in partition_diffs



if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1, 2, 3]))
    print(s.canPartition([1,2,3,4,5,6,7]))
    # print(s.canPartition([1, 5, 11, 5]))
    # print(s.canPartition([1,2,3,5]))
