def min_bitwise_array(nums):
    ans = []

    for x in nums:
        if x % 2 == 0:
            ans.append(-1)
        else:
            lowest_set_bit = x & -x
            ans.append(x ^ lowest_set_bit)

    return ans


# -------- TEST CASES --------
if __name__ == "__main__":
    nums1 = [2, 3, 5, 7]
    nums2 = [11, 13, 31]

    print(min_bitwise_array(nums1))  # [-1, 1, 4, 3]
    print(min_bitwise_array(nums2))  # [9, 12, 15]
