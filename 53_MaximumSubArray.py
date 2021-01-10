from typing import List


class Solution:
    def maxSubArray(self, nums: List[int], s, d, st_ind, end_ind, curr_max) -> int:
        print("Received", nums, sum(nums), s, d, st_ind, end_ind)
        if len(nums) == 1:
            return nums[0], st_ind, end_ind
        split = len(nums)//2
        lsum, l_st_ind, l_end_ind = self.maxSubArray(
            nums[:split], "left", d+1, st_ind, st_ind + split - 1, curr_max)
        rsum, r_st_ind, r_end_ind = self.maxSubArray(
            nums[split:], "right", d+1, st_ind + split, end_ind, curr_max)
        curr_max = max(curr_max, sum(nums[:split]), sum(nums[split:]))
        print("Final", nums, d, "lsum", lsum, "rsum", rsum,
              l_st_ind, l_end_ind, r_st_ind, r_end_ind)
        # Check for contiguous
        if (l_end_ind + 1 == r_st_ind):
            return max(lsum, rsum, lsum + rsum), l_end_ind, l_end_ind
        else:
            return max(lsum, rsum, lsum+rsum), l_st_ind, l_end_ind


if __name__ == '__main__':
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-1, -2, 3, 4]
    st_ind = 0  # Mapping to orignal index
    end_ind = len(nums) - 1  # Mapping to original index
    d = 0  # Depth
    curr_max = sum(nums)
    curr_max, l_ind, r_ind = sol.maxSubArray(
        nums, "first", d, st_ind, end_ind, curr_max)
    print("curr_max", curr_max)
