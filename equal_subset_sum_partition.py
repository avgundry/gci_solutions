from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        partition_diffs = set()
        partition_diffs.add(nums[0])
        partition_diffs.add(-nums[0])


        for i in range(1, len(nums)):
            # calculate the partition differences 
            # partition_diffs.append([0] * len(partition_diffs[i-1]) * 2)
            # for j in range(i):
            #     print(partition_diffs[i - 1])
            curr = nums[i]
            curr_lvl = set()
            for diff in partition_diffs:
                curr_lvl.add(diff + curr)
                curr_lvl.add(diff - curr)
            partition_diffs = curr_lvl

        return 0 in partition_diffs


if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1, 2, 3]))
    print(s.canPartition([1,2,3,4,5,6,7]))
    # print(s.canPartition([1, 5, 11, 5]))
    # print(s.canPartition([1,2,3,5]))
