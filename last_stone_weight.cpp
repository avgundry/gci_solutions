// solving as precursor to Last Stone Weight II, which is a DP problem
#include <iostream>
#include <vector>


class Solution {
public:
    int lastStoneWeight(std::vector<int>& stones) {
        // hm. what's the optimal way to do this?
        // heap sort of some kind into a max heap seems ideal.....
        // O(n*log(n)) time to do that, though. is there O(n) time?

        // smaller stone
        int x;
        // bigger stone
        int y;
        // return val
        int ret = 0;
        std::vector<int> max_heap = std::vector<int>();
        std::make_heap(max_heap.begin(), max_heap.end());

        for (int stone: stones) {
            max_heap.push_back(stone);
            push_heap(max_heap.begin(), max_heap.end());
        }

        while (max_heap.size() > 1) {
            int y = max_heap.front();
            pop_heap(max_heap.begin(), max_heap.end());
            int x = max_heap.front();
            pop_heap(max_heap.begin(), max_heap.end());
            max_heap.pop_back();
            max_heap.pop_back();
            if (x != y) {
                max_heap.push_back(y - x);
                push_heap(max_heap.begin(), max_heap.end());
            }
        }

        if (!max_heap.empty()) {
            ret = max_heap.front();
        }

        return ret;

    }
};

int main() {
    Solution s;
    std::vector<int> stones = std::vector<int>{2,7,4,1,8,1};
    std::cout << "TEST" << std::endl;
    std::cout << s.lastStoneWeight(stones) << std::endl;
}
