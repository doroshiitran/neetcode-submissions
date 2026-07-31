class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # mid = nums.len/2
        # target > mid, start from the right, and opposite
        base = -1
        middle = len(nums) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            for i in range(middle):
                if nums[i] == target:
                    return i
            return base
        elif nums[middle] < target:
            for i in range(middle, len(nums)):
                if nums[i] == target:
                    return i
            return base
        else:
            return base
