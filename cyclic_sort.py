def cyclic_sort(nums):
    num_sorted = 0
    i = 0

    while num_sorted != len(nums) and i < len(nums):
        curr = nums[i]
        if curr == i + 1:
            # num_sorted += 1
            i += 1
        else:
            temp = nums[curr - 1]
            while temp != curr:
                nums[curr - 1] = curr
                num_sorted += 1
                curr = temp
                temp = nums[curr - 1]
            num_sorted += 1
            i += 1



    return nums

if __name__ == "__main__":
    assert cyclic_sort([3, 1, 5, 4, 2]) == [1, 2, 3, 4, 5]
    assert cyclic_sort([2, 6, 4, 3, 1, 5]) == [1, 2, 3, 4, 5, 6]
    assert cyclic_sort([1, 5, 6, 4, 3, 2]) == [1, 2, 3, 4, 5, 6]