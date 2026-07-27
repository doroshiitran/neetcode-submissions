class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        pivot = 0
        while pivot < len(nums):
            l = pivot +1
            r = len(nums)-1
            if pivot > 0 and nums[pivot] == nums[pivot-1]:
                pivot +=1
                continue
            # -4, -1, -1, 0, 1, 2
            while l < r:
                sum = nums[pivot] + nums[l] + nums[r]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    ans.add(tuple(sorted([nums[pivot], nums[l], nums[r]])))
                    l+=1
                    r-=1
            pivot+=1
        return list(ans)