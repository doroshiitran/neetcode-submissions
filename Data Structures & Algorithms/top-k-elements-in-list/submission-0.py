class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        placeholder={}
        for num in nums:
            if num not in placeholder:
                placeholder[num]=1
            else:
                placeholder[num]+=1
        sorted_nums = sorted(placeholder.items(), key = lambda x:x[1],reverse=True)
        ans = []
        for key, values in sorted_nums[:k]:
            ans.append(key)
        return ans

