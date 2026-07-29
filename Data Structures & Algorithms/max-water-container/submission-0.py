class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # pointer 1 l=0 1 r=len(heights-1)
        # ans = 0
        # i = 0; i++ => h = min(height[l],height[r]), max =  h * (r-l), if max > ans : max = ans
        l = 0
        r = len(heights) -1
        ans = 0
        while l < r:
            h = min(heights[l],heights[r])
            max_area= h * (r-l)
            ans = max(ans, max_area)
            if heights[l] < heights[r]:
                l +=1
            else:
                r -=1
        return ans