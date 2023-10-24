#include <algorithm>
#include <map>
#include <vector>

class KthLargest {
public:
    int k;
    std::vector<int> min_heap;

    KthLargest(int k, std::vector<int>& nums) {
        this->k = k;
        // at first make it a standard freq map with num:freq pairs
        // then convert to a bucket map.
        std::make_heap(this->min_heap.begin(), this->min_heap.end(), std::greater<>{});
    }
    
    int add(int val) {
        // increment val in our frequency map
        if (this->min_heap.size() < k) {
            std::push_heap(this->min_heap.begin(), this->min_heap.end());
        }
        else {
            std::push_heap(this->min_heap.begin(), this->min_heap.end());
        }
        return this->min_heap.at(0);
    }
};

int main() {
    // I've forgotten all my c++; debug this later
    KthLargest s = new KthLargest(3, std::vector<int>{4, 5, 8, 2});
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */