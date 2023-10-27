#include <iostream>
#include <vector>

class Solution {
public:
    int lastStoneWeightII(std::vector<int>& stones) {
       // hmmm...this FEELS like a DP problem. 
       // perhaps..at each step, what is the MOST we can reduce the list by?
       // by knocking out both stones I guess? or...no...fuck.
       // it'll always be by choosing the largest two stones. won't it? 
       // at least for that individual step...yeah. cause you reduce it by the second
       // largest, which is the most you can do.

       // at the last step, say we have stones a,b. We want to MINIMIZE a - b.
       // There's no actual choices there so let's look at the step before.
       // At the step before that we would have had stones s1, s2, s3.
       // We choose to choose such that the two remaining stones are as small as possible.
       // Let's say s1 >= s2 >= s3.
       // Then...
       // We want to choose stones i,j such that with the remaining stone h we minimize
       // (s_i - s_j) - s_h. How do we do that?  
       // Choose two stones whose difference is closest to s_h..?


       // utterly brute force method: recursively find the minimum of EVERY
       // possible permutation
       // hm. this is a permutation of indices? or...

       // reduce to a knapsack problem.
       // at the end we will have two sums: sum1 - sum2 = answer.
       // sum2 <= sum1 since negative answer not possible.
       // we have sum1 + sum2 = sum of all elements.
       // thus sum1 = sumall - sum2, thus sum1 - sum2 = sumall - 2*sum2.
       // want to minimize sumall - 2*sum2.
       // same as wanting to maximize sum2. We have sumall - 2*sum2 >= 0;
       // thus sumall/2 >= sum2
       // find CLOSEST SUM <= sumall/2.
       // can be thought of as knapsack problem...where we have that 
       // for each item, weight = value.
       // thus want to maximize value without going over weight capacity of
       // total sum / 2.

       // begin by finding total
       int total = 0;
       for (int w: stones) {
        total += w;
       }

       // naive solution is to recursively loop over all of the numbers
       // if the sum of a given combination <= total / 2, add it to list
       // call recursion func I guess.
       return recurseStone(stones, total / 2, stones.size());
    }

    int recurseStone(std::vector<int>& stones, int capacity, int n) {
        // base cases
        if (n == 1) {
            return stones.front();
        }
        if (n == 0 or capacity == 0) {
            return 0;
        }

        // check if weight of nth item < capacity
        if (stones.at(n-1) <= capacity) {
            return std::max(
                stones[n - 1] + recurseStone(stones, capacity - stones[n - 1], n - 1),
                recurseStone(stones, capacity, n - 1)
            );
        }
        else {
            return recurseStone(stones, capacity, n - 1);
        }
    }
};

int main() {
    Solution s;
    std::vector<int> v = std::vector<int>{2,7,4,1,8,1};
    std::cout << s.lastStoneWeightII(v) << std::endl;
}