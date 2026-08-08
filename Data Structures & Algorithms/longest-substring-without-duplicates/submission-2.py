class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        hash_set={}, max=0, count=0 for char in s:
        if char not in hash_set:            hash_set.add(char), count+=1 else: max(count, max)
        """
        hash_set= set()
        max_len=0
        l, r = 0, 0
        while r<len(s):
            if s[r] not in hash_set:
                hash_set.add(s[r])
                current_len=r-l+1
                max_len=max(max_len,current_len)
                r+=1
            else:
                hash_set.remove(s[l])
                l+=1
        return max_len