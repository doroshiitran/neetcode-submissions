class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles[i]: number of bananas
        # h: hours to eat all banana
        # k: minimum eating rate per hours to eat all banana
        # pile < k => finish eat, couldnt eat another pile same hour
        piles.sort()
        left = 1
        right = piles[-1]
        while left <= right:
            mid = (left+right) //2
            hours =0
            for pile in piles:
                hours += (pile+mid-1) // mid
            if hours <=h:
                right = mid-1
            else:
                left = mid + 1
        return left