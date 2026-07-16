class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ 
            O(n^2)
            1. loop through list nums (i,j)
            2. if nums[j+1]<= nums[j] => hashmap.append(nums[j])
            if nums[j+1]> nums[j] => i+1, j=i
            3. hashmap.sort(desc()length(hashmap)) => return value.hashmap(0)
        """
        """
            O(n^2)

        """
        longest_streak = 0
        for i in range(len(nums)):
            current_num = nums[i]
            current_streak = 1
            
            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak